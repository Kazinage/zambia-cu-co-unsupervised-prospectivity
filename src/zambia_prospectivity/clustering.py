"""Core unsupervised ensemble used for the Zambia portfolio implementation."""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import skfuzzy as fuzz
from minisom import MiniSom
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


FEATURES = [
    "Grav_THD",
    "Mag_THD",
    "Mag_Tilt_Derivative",
    "Mag_Analytical_Signal",
    "U_Th",
    "U_K",
]


@dataclass
class EnsembleResult:
    scaled: np.ndarray
    scaler: StandardScaler
    kmeans_labels: np.ndarray
    fcm_labels: np.ndarray
    fcm_membership: np.ndarray
    som_labels: np.ndarray
    consensus_labels: np.ndarray


def choose_k(X, candidates=range(2, 7), random_state=42):
    """Return silhouette scores for candidate KMeans partitions."""
    X = np.asarray(X, dtype=float)
    return {
        int(k): float(
            silhouette_score(
                X,
                KMeans(n_clusters=k, n_init=20, random_state=random_state).fit_predict(X),
            )
        )
        for k in candidates
    }


def fit_ensemble(X, *, k=3, som_shape=(6, 6), random_state=42):
    """Fit KMeans, FCM and SOM, then cluster their label triplets."""
    X = np.asarray(X, dtype=float)
    scaler = StandardScaler().fit(X)
    Z = scaler.transform(X)

    km_labels = KMeans(
        n_clusters=k, n_init=30, random_state=random_state
    ).fit_predict(Z)

    _, u, _, _, _, _, _ = fuzz.cluster.cmeans(
        Z.T, c=k, m=2.0, error=1e-5, maxiter=1000, seed=random_state
    )
    fcm_labels = np.argmax(u, axis=0)

    som = MiniSom(
        som_shape[0],
        som_shape[1],
        Z.shape[1],
        sigma=1.0,
        learning_rate=0.5,
        random_seed=random_state,
    )
    som.random_weights_init(Z)
    som.train_random(Z, num_iteration=max(2000, len(Z)))

    weights = som.get_weights().reshape(-1, Z.shape[1])
    neuron_group = KMeans(
        n_clusters=k, n_init=30, random_state=random_state
    ).fit_predict(weights)
    som_labels = np.array(
        [neuron_group[w[0] * som_shape[1] + w[1]] for w in map(som.winner, Z)]
    )

    label_matrix = np.column_stack([km_labels, fcm_labels, som_labels])
    consensus = KMeans(
        n_clusters=k, n_init=50, random_state=random_state
    ).fit_predict(label_matrix)

    return EnsembleResult(
        scaled=Z,
        scaler=scaler,
        kmeans_labels=km_labels,
        fcm_labels=fcm_labels,
        fcm_membership=u.T,
        som_labels=som_labels,
        consensus_labels=consensus,
    )


def cluster_means(X, labels):
    X = np.asarray(X, dtype=float)
    labels = np.asarray(labels)
    return {int(c): X[labels == c].mean(axis=0) for c in np.unique(labels)}

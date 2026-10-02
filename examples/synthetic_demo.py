"""Synthetic demonstration of the ensemble clustering API."""

import numpy as np

from zambia_prospectivity.clustering import choose_k, fit_ensemble, cluster_means
from zambia_prospectivity.prospectivity import target_membership, prospectivity_class


rng = np.random.default_rng(7)
n = 4500

latent = rng.choice(3, size=n, p=[0.55, 0.30, 0.15])
centres = np.array([
    [0.0, 0.0, -0.2, -0.1, -0.1, -0.2],
    [0.4, 0.7, 0.5, 0.6, 0.2, 0.3],
    [1.5, 1.7, 1.3, 1.6, 1.2, 1.4],
])
X = centres[latent] + rng.normal(0, 0.55, size=(n, 6))

print("Silhouette:", choose_k(X))
result = fit_ensemble(X, k=3)
means = cluster_means(result.scaled, result.consensus_labels)

# Demo-only choice. The paper selected its target using literature benchmarks.
target = max(means, key=lambda c: means[c].mean())
score = target_membership(result.fcm_membership, target)
classes = prospectivity_class(score)

print("Target cluster:", target)
print("Prospectivity class counts:", dict(zip(*np.unique(classes, return_counts=True))))

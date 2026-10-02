"""Prospectivity scoring from fuzzy membership."""

from __future__ import annotations

import numpy as np


def target_membership(fcm_membership, target_cluster: int):
    """Continuous similarity to the selected FCM target cluster."""
    u = np.asarray(fcm_membership, dtype=float)
    return u[:, int(target_cluster)]


def prospectivity_class(score, medium=0.5, high=0.8):
    """Classify membership using the decision thresholds used in the study."""
    s = np.asarray(score, dtype=float)
    out = np.full(len(s), "Low", dtype=object)
    out[s >= medium] = "Medium"
    out[s >= high] = "High"
    return out


def cluster_benchmark_score(cluster_mean, lower_bounds):
    """Count standardized features meeting supplied analogue lower bounds.

    Threshold values are supplied by the caller because published analogue
    thresholds are context-dependent and should not be silently transferred
    to a new survey.
    """
    mean = np.asarray(cluster_mean, dtype=float)
    lower = np.asarray(lower_bounds, dtype=float)
    if mean.shape != lower.shape:
        raise ValueError("cluster_mean and lower_bounds must have the same shape")
    return int(np.sum(mean >= lower))

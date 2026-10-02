# Methodology notes

## Survey and preprocessing

The study used a high-resolution airborne survey over the southern margin of the Central African Copperbelt in northern Zambia. Gravity, magnetics, radiometrics and terrain products were harmonized to a common 50 m grid in WGS 84 / UTM Zone 35S.

The published analysis considered a broader transformed stack, then retained six variables for clustering and external signature benchmarking:

- gravity total horizontal derivative;
- magnetic total horizontal derivative;
- magnetic tilt derivative;
- magnetic analytic signal amplitude;
- U/Th;
- U/K.

All retained features were standardized to zero mean and unit variance.

## Ensemble clustering

Three algorithms were fitted independently to the same standardized feature matrix.

### K-Means

Solutions around k=3 and k=4 were examined. Elbow and silhouette diagnostics supported k=3 for the final ensemble.

### Fuzzy C-Means

FCM used fuzzifier m=2. Membership values preserve gradational transitions and provide the continuous score used for the final prospectivity map.

### Self-Organizing Map

A 6x6 SOM represented the six-dimensional feature space with 36 prototype neurons. SOM codebook vectors were subsequently grouped into three classes.

### Consensus

The three hard label vectors (K-Means, argmax FCM, grouped SOM) form an N x 3 label matrix. A second K-Means partition with k=3 is fitted to that label matrix to emphasize patterns persistent across algorithms.

## Target-cluster selection

Cluster labels are arbitrary. The target cluster must therefore be selected using geological/geophysical evidence, not by assuming that cluster 0 or cluster 1 is always prospective.

In the publication, consensus-cluster summary statistics were compared with literature-derived geophysical intervals. Standardized and log-transformed comparisons supported the same priority domain.

The code deliberately requires benchmark thresholds to be passed explicitly rather than embedding analogue values as universal constants.

## Continuous prospectivity

After selecting the geophysically plausible target domain, FCM membership to that cluster is used as a continuous similarity score.

The study used:

- Low: 0.0 <= membership < 0.5
- Medium: 0.5 <= membership < 0.8
- High: 0.8 <= membership <= 1.0

## Interpretation boundary

This is an unsupervised targeting workflow. It identifies multivariate geophysical similarity, not ore directly. The original study had no drill-hole ground truth for conventional supervised accuracy assessment, so geological follow-up remains essential.

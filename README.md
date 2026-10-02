# Zambia Cu-Co Unsupervised Prospectivity

**Ensemble unsupervised targeting from airborne gravity, magnetics and radiometrics in a label-scarce exploration setting.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.55452%2F1998--6688--2026--23--2--435--450-blue)](https://doi.org/10.55452/1998-6688-2026-23-2-435-450)

Reference implementation of the workflow described in:

> **Saduov, A. (2026).** *Unsupervised Delineation of Prospectivity Zones for Stratiform Cu-Co in the Southern Copperbelt Margin (Zambia).*  
> **Herald of the Kazakh-British Technical University, 23(2), 435-450.**  
> https://doi.org/10.55452/1998-6688-2026-23-2-435-450

## Problem

Greenfield exploration commonly lacks reliable deposit labels and verified barren examples. Instead of forcing a supervised classifier onto uncertain labels, this project treats airborne geophysical signatures as an unsupervised domain-discovery problem.

The study integrates three complementary clustering families:

- **K-Means** for compact hard partitions;
- **Fuzzy C-Means (FCM)** for gradual membership and continuous prospectivity;
- **Self-Organizing Maps (SOM)** for topology-preserving representation;
- a **consensus partition** to reduce dependence on any single algorithm.

## Input evidence

The published workflow began with gravity, magnetics, radiometrics and terrain. Six diagnostic variables were retained for the clustering/benchmarking stage:

| Feature | Exploration role |
|---|---|
| Gravity THD | lateral density contrasts / structural edges |
| Magnetic THD | magnetic boundaries and lineaments |
| Magnetic tilt derivative | subtle edges and shallow sources |
| Magnetic analytic signal | source-centred magnetic response |
| U/Th | radiometric contrast / alteration proxy |
| U/K | radiometric contrast / alteration proxy |

All analysis layers were co-registered on a **50 m grid in WGS 84 / UTM Zone 35S** and standardized before clustering.

## Workflow

```text
Airborne gravity + magnetics + radiometrics + terrain
                         |
                         v
             Geophysical transformations
                         |
                         v
          Six diagnostic exploration features
                         |
                         v
                 StandardScaler
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
       K-Means          FCM            SOM 6x6
          |              |              |
          +--------------+--------------+
                         |
                         v
              Consensus clustering
                         |
                         v
      Literature-calibrated signature check
                         |
                         v
        Select geophysically plausible cluster
                         |
                         v
          FCM membership to target cluster
                         |
                         v
      Low <0.5 | Medium 0.5-0.8 | High >=0.8
```

## Published interpretation

The paper selected **k = 3** based on elbow and silhouette diagnostics. The consensus priority domain was supported by comparison with literature-derived geophysical anomaly ranges. The final continuous map used FCM membership to the selected target cluster.

The selected prospective cluster occupied approximately **12% of the survey area**. High-prospectivity membership was concentrated mainly along the southern and southeastern parts of the survey area.

This is an early-stage targeting result. The publication explicitly notes that the absence of drilling and systematic local geochemical labels prevents conventional accuracy assessment.

## Repository structure

```text
.
├── data/README.md
├── docs/methodology.md
├── examples/synthetic_demo.py
├── src/zambia_prospectivity/
│   ├── __init__.py
│   ├── clustering.py
│   └── prospectivity.py
├── CITATION.cff
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

## Quick start

```bash
git clone https://github.com/Kazinage/zambia-cu-co-unsupervised-prospectivity.git
cd zambia-cu-co-unsupervised-prospectivity
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
python examples/synthetic_demo.py
```

## Reproducibility and data

The code is a clean **reference implementation of the published methodology**. The historical research code and large airborne grids are not redistributed here. The demo uses synthetic data.

The study used a publicly released airborne dataset accessed through a public data portal. Mention of the survey/data source does not imply employment, sponsorship, endorsement or a commercial relationship between the repository author and the data producer.

## Scientific limitations

- Unsupervised similarity is not proof of mineralization.
- Literature-derived thresholds are analogues, not local ground truth.
- Radiometric signatures can be modified by regolith and weathering.
- Potential-field anomalies are non-unique.
- Drill-hole, geochemical and geological follow-up are required before target advancement.

## Author

**Alisher Saduov, PhD**  
Geophysics | Mineral Exploration | GeoAI | Spatial Machine Learning  
Satbayev University, Kazakhstan  
ORCID: 0000-0003-1501-7772

## License

Code is MIT licensed. External datasets remain under their original licenses and terms.

# Data notes

The original airborne grids are not redistributed in this repository.

The research workflow used gravity, magnetic, radiometric and terrain information from a publicly released airborne survey dataset. Users should obtain source data from the original public distribution channel and comply with its license and attribution requirements.

## Expected modelling table

The reference implementation expects six numeric columns in this order:

```text
Grav_THD
Mag_THD
Mag_Tilt_Derivative
Mag_Analytical_Signal
U_Th
U_K
```

Coordinates may be retained separately for mapping but are not used as clustering features.

## Important

This repository is not affiliated with, endorsed by, or sponsored by the original survey/data producer. It is an independent academic reference implementation of the published workflow.

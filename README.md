# Copper Production Geography Dryness Demo

This repository is a minimal, public-safe demonstration package for the study:

**Production geography concentrates dryness exposure in global copper supply**

The package reproduces demonstration figures from derived, non-restricted tables only. It is intentionally **not** a raw-data repository and does not redistribute raw CHIRPS files, raw mine-point inventories, manuscript submission files, or local working caches.

## Contents

```text
data/
  figure1_production_geography_source_data.csv
  figure2_cpwe_gli_coverage_source_data.csv
  figure3_top_country_contribution_source_data.csv
  figure4_controls_source_data.csv
  manuscript_authority_table.csv
  supplementary_data_index.csv
scripts/
  build_demo_figures.py
outputs/
  Figure_1_Share_Exposure_Scatter_Demo.{png,pdf,svg}
  Figure_2_CPWE_GLI_Coverage_Demo.{png,pdf,svg}
  Figure_3_Top_Country_Contribution_Demo.{png,pdf,svg}
  Figure_4_Controls_Demo.{png,pdf,svg}
DATA_PROVENANCE.md
SANITIZATION_REPORT.md
manifest_public_demo_20260526.md
requirements.txt
```

## What This Demo Shows

The demo preserves the study's evidence boundary:

- production geography weights dryness exposure rather than simple spatial averaging;
- copper ranks first by country-production-weighted exposure in the six-metal comparison set;
- top-country structure is dominated by Chile, DR Congo, Peru, and Zambia;
- controls bound unusual allocation and single-country dominance.

The demo does **not** claim:

- supply interruption;
- price transmission;
- causal attribution;
- a completed multi-metal mechanism.

## Rebuild The Demo Figures

Create an environment with Python 3, `pandas`, and `matplotlib`, then run:

```bash
python scripts/build_demo_figures.py
```

The script writes PNG, PDF, and SVG outputs into `outputs/`.

## Data Boundary

Included:

- figure-ready derived source tables for Figures 1-4;
- a manuscript authority table for value traceability;
- a supplementary data index for file-level provenance.

Not included:

- raw CHIRPS, NetCDF, Zarr, or mine-node extraction products;
- manuscript DOCX, cover letters, declarations, or submission forms;
- large caches, logs, null-draw archives, or local machine paths.

## License

No open-source license has been assigned yet. Until a license is added, all rights are reserved.

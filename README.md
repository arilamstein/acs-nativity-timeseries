# ACS Nativity Time Series

This repository contains a small, focused analysis of nativity trends in the United States and in Minneapolis, Minnesota, using the American Community Survey (ACS) 1‑year estimates. The project uses the `censusdis` Python package to pull ACS table **B05012 (Nativity in the United States)** across multiple years and visualize changes over time.

The repo includes:
- a lightweight plotting module (`graphs.py`)
- a national‑level notebook (`nation.ipynb`)
- a Minneapolis‑specific notebook (`minneapolis.ipynb`)

The goal is to make it easy to reproduce the analysis, adapt it to other geographies, or reuse the plotting function for other ACS time‑series work.

---

## Data Source

All data comes from the **ACS 1‑Year Estimates**, table **B05012: Nativity**, accessed via the `censusdis` package.

Years included: **2009–2024**, excluding **2020** (no 1‑year ACS release due to the pandemic).

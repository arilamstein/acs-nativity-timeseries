# ACS Nativity Time Series

This repository contains a small, focused analysis of nativity trends in the United States and in Minneapolis, Minnesota, using the American Community Survey (ACS) 1‑year estimates.

The repo includes:
- a lightweight module for ingesting the data (`data.py`)
- a lightweight plotting module (`plotting.py`)
- a national‑level notebook (`nation.ipynb`)
- a Minneapolis‑specific notebook (`minneapolis.ipynb`)

The goal is to make it easy to reproduce the analysis, adapt it to other geographies, or reuse the plotting function for other ACS time‑series work.

---

## Data Source

All data comes from the **ACS 1‑Year Estimates**, tables `B05002` (2005-2008) and `B05012` (2009-2024), accessed via the `censusdis` package.

Note: No 1-year ACS was published for **2020** due to Covid-19.

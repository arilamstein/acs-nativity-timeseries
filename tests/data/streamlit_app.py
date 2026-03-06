"""
Streamlit app used for manually testing title and label generation in the
plotting functions across different columns and geographies.
"""

import pandas as pd
import streamlit as st

from acs_nativity import plot_nativity_timeseries, plot_nativity_change


DATASETS = {
    "United States": "data_us.csv",
    "State": "data_state.csv",
    "County": "data_county.csv",
    "Place": "data_place.csv",
}

COLUMNS = [
    "Total",
    "Native",
    "Foreign-born",
    "Percent Foreign-born",
]


st.title("ACS Nativity Explorer")

dataset_name = st.selectbox("Choose a geography dataset", list(DATASETS.keys()))
df = pd.read_csv(DATASETS[dataset_name])

column = st.selectbox("Choose a column to visualize", COLUMNS)

col1, col2 = st.columns(2)

fig1 = plot_nativity_timeseries(df, column=column)
st.plotly_chart(fig1)

fig2 = plot_nativity_change(df, column=column)
st.plotly_chart(fig2)

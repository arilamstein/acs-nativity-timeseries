"""Test the data.py module."""

import pandas as pd
from acs_nativity import data


EXPECTED_COLUMNS = ["Name", "Year", "Total", "Native", "Foreign-born"]


def test_normalize_columns_2008():
    """
    Test that we normalize columns from the 2008 data as expected. Use 2008
    because it is the last year of data from the first table we download, and
    censusdis.download_multiyear uses the column names from the of the last
    year of a multi-year period.
    """
    df_2008 = pd.DataFrame(
        {
            "US": {0: "1"},
            "Total": {0: 304059728},
            "Native": {0: 266098793},
            "Born in state of residence": {0: 179132918},
            "Born in other state in the United States": {0: 82935072},
            "Northeast": {0: 19834782},
            "Midwest": {0: 22663702},
            "South": {0: 26007650},
            "West": {0: 14428938},
            "Born outside the United States": {0: 4030803},
            "Puerto Rico": {0: 1441567},
            "U.S. Island Areas": {0: 177776},
            "Born abroad of American parent(s)": {0: 2411460},
            "Foreign born": {0: 37960935},
            "Naturalized U.S. citizen": {0: 16329909},
            "Not a U.S. citizen": {0: 21631026},
            "GEO_ID": {0: "0100000US"},
            "NAME": {0: "United States"},
            "Year": {0: 2008},
        }
    )
    df_out = data._normalize_columns(df_2008)
    assert list(df_out.columns) == EXPECTED_COLUMNS


def test_normalize_columns_2024():
    """
    Test that we normalize columns from the 2024 data as expected. Use 2024
    because it is the last year of data from the second table we download, and
    censusdis.download_multiyear uses the column names from the of the last
    year of a multi-year period.
    """
    df_2024 = pd.DataFrame(
        {
            "US": {0: "1"},
            "Total": {0: 340110990},
            "Native": {0: 289876132},
            "Foreign-born": {0: 50234858},
            "GEO_ID": {0: "0100000US"},
            "NAME": {0: "United States"},
            "Year": {0: 2024},
        }
    )
    df_out = data._normalize_columns(df_2024)
    assert list(df_out.columns) == EXPECTED_COLUMNS

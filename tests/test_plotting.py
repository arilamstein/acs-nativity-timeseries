"""Test the plotting.py module."""

import pytest
import pandas as pd
import acs_nativity.plotting as plotting
from plotly.graph_objs import Figure


@pytest.fixture
def df_us():
    """Return a sample dataframe of us data."""
    return pd.DataFrame(
        {
            "Name": ["United States"],
            "Year": [2009],
            "Total": [110],
            "Native": [85],
            "Foreign-born": [25],
            "Percent Foreign-born": [0.5],
        }
    )


def test_timeseries_title_bad_input(df_us):
    """Test that _generate_timeseries_title throws an exception with bad input."""
    with pytest.raises(ValueError):
        plotting._generate_timeseries_title(df_us, "foo")

    df_sf = pd.DataFrame(
        {
            "Name": {0: "San Francisco County, California"},
            "Year": {0: 2005},
            "Total": {0: 719077},
            "Native": {0: 461508},
            "Foreign-born": {0: 257569},
            "Percent Foreign-born": {0: 35.819390691122095},
        }
    )

    df_combined = pd.concat([df_us, df_sf])
    with pytest.raises(ValueError):
        plotting._generate_timeseries_title(df_combined, "Total")


def test_timeseries_title_good_input(df_us):
    """Test that _generate_timeseries_title returns the correct title with good input."""
    assert (
        plotting._generate_timeseries_title(df_us, "Percent Foreign-born")
        == "Percent Foreign-born in the United States"
    )
    assert (
        plotting._generate_timeseries_title(df_us, "Foreign-born")
        == "Foreign-born Population in the United States"
    )


def test_generate_change_title(df_us):
    """Test generating title for the "change in" visualization."""
    assert (
        plotting._generate_change_title(df_us, "Foreign-born")
        == "Change in Foreign-born Population in the United States"
    )


def test_generate_timeseries_y_label():
    assert plotting._generate_change_y_label("Percent Foreign-born" == "Percent")
    assert plotting._generate_change_y_label("Foreign-born" == "Population")


@pytest.mark.parametrize(
    "column",
    [
        "Total",
        "Native",
        "Foreign-born",
        "Percent Foreign-born",
    ],
)
def test_plot_nativity_timeseries_all_columns(df_us_2024, column):
    fig = plotting.plot_nativity_timeseries(df_us_2024, column=column)
    assert isinstance(fig, Figure)


@pytest.mark.parametrize(
    "column",
    [
        "Total",
        "Native",
        "Foreign-born",
        "Percent Foreign-born",
    ],
)
def test_plot_nativity_change_all_columns(df_us_2024, column):
    fig = plotting.plot_nativity_change(df_us_2024, column=column)
    assert isinstance(fig, Figure)

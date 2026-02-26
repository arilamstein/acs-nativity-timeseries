from censusdis.multiyear import download_multiyear
from censusdis.datasets import ACS1
import pandas as pd


def get_full_acs1_nativity_timeseries(**kwargs):
    # From 2005-8 the data we want is in table B05002
    df1 = download_multiyear(
        dataset=ACS1,
        vintages=[year for year in range(2005, 2009)],
        group="B05002",
        **kwargs,
    )
    # This table has columns that are not present in B05012, so subset them.
    # Also, rename a column so it matches spelling in B05012
    df1 = df1[["Total", "Native", "Foreign born", "Year"]]
    df1 = df1.rename(columns={"Foreign born": "Foreign-born"})

    # In later years, use B05012. Note that no ACS1 was published in 2020
    df2 = download_multiyear(
        dataset=ACS1,
        vintages=[year for year in range(2009, 2025) if year != 2020],
        group="B05012",
        **kwargs,
    )

    return pd.concat([df1, df2])

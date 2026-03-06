"""
Public API for the acs_nativity package.

Provides functions for downloading ACS 1-year nativity data across years and
utilities for visualizing nativity levels and changes over time.
"""

from importlib.metadata import version

from .data import get_nativity_timeseries
from .plotting import (
    plot_nativity_timeseries,
    plot_nativity_change,
)

__version__ = version("acs-nativity")

__all__ = [
    "get_nativity_timeseries",
    "plot_nativity_timeseries",
    "plot_nativity_change",
]

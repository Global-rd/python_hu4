"""
Dashboard-level data types.
"""

from typing import TypedDict


class DashboardLocation(TypedDict):
    """Location shape used by the dashboard after geocoding."""

    # Stable Open-Meteo location identifier.
    id: int
    # Display name of the city or settlement.
    name: str
    # Location latitude used by the forecast and map views.
    latitude: float
    # Location longitude used by the forecast and map views.
    longitude: float
    # Country label displayed in dashboard text and logs.
    country: str
    # Full autocomplete label displayed in the searchbox.
    label: str


# Searchbox option containing a display label and its dashboard location.
type LocationSearchOption = tuple[str, DashboardLocation]

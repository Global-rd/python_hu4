"""
Location search service for the weather dashboard.
"""

from collections.abc import Mapping
from typing import cast

import streamlit as st

from ..app_types import DashboardLocation
from ..open_meteo import (
    CityLocation,
    GeocodingSearchParams,
    OpenMeteoClient,
)


class LocationSearchService:
    """Search and adapt Open-Meteo geocoding locations."""

    GEOCODING_LANGUAGE: str = "en"
    GEOCODING_FORMAT: str = "json"
    API_CACHE_TTL_SECONDS: int = 60 * 60

    def __init__(
        self,
        geocoding_result_count: int,
        min_search_term_length: int,
    ) -> None:
        """Initialize the service with search configuration."""
        self.geocoding_result_count: int = geocoding_result_count
        self.min_search_term_length: int = min_search_term_length

    @staticmethod
    @st.cache_data(ttl=API_CACHE_TTL_SECONDS, show_spinner=False)
    def _search_cities_cached(
        params: GeocodingSearchParams,
    ) -> list[CityLocation]:
        """Return cached geocoding results for one hour."""
        return OpenMeteoClient().search_cities(params)

    @staticmethod
    def _get_optional_location_value(
        location: CityLocation,
        key: str,
    ) -> str | None:
        """Return an optional geocoding field as text."""
        raw_location: Mapping[str, object] = cast(
            Mapping[str, object],
            location,
        )
        value: object | None = raw_location.get(key)

        if value is None or value == "":
            return None

        return str(value)

    @classmethod
    def _create_location_label(cls, location: CityLocation) -> str:
        """Return a readable search result label from an API location."""
        label_parts: list[str | None] = [
            location["name"],
            cls._get_optional_location_value(location, "admin1"),
            cls._get_optional_location_value(location, "country")
            or cls._get_optional_location_value(location, "country_code"),
        ]
        visible_label_parts: list[str] = [
            label_part for label_part in label_parts if label_part is not None
        ]

        return ", ".join(visible_label_parts)

    @classmethod
    def _to_dashboard_location(
        cls,
        location: CityLocation,
    ) -> DashboardLocation:
        """Convert an Open-Meteo location to the dashboard location shape."""
        country: str = (
            cls._get_optional_location_value(location, "country")
            or cls._get_optional_location_value(location, "country_code")
            or "Unknown country"
        )

        return {
            "id": location["id"],
            "name": location["name"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "country": country,
            "label": cls._create_location_label(location),
        }

    def _create_geocoding_search_params(
        self,
        city_name: str,
    ) -> GeocodingSearchParams:
        """Return Open-Meteo geocoding search params for the app."""
        return {
            "name": city_name.strip(),
            "count": self.geocoding_result_count,
            "language": self.GEOCODING_LANGUAGE,
            "format": self.GEOCODING_FORMAT,
        }

    def search_locations(self, search_term: str) -> list[DashboardLocation]:
        """Return geocoding autocomplete results for a search term."""
        normalized_search_term: str = search_term.strip()

        if len(normalized_search_term) < self.min_search_term_length:
            return []

        search_term_has_letter: bool = any(
            character.isalpha() for character in normalized_search_term
        )

        if not search_term_has_letter:
            return []

        locations: list[CityLocation] = self._search_cities_cached(
            self._create_geocoding_search_params(normalized_search_term)
        )

        return [
            self._to_dashboard_location(location) for location in locations
        ]

    def get_default_location(self, default_city: str) -> DashboardLocation:
        """Return the dashboard location for the configured default city."""
        locations: list[DashboardLocation] = self.search_locations(
            default_city
        )

        if len(locations) == 0:
            raise ValueError(f"City not found: {default_city}")

        return locations[0]

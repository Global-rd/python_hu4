"""
Application-level configuration for the weather dashboard.
"""

from collections.abc import Mapping
from typing import cast

import streamlit as st


class AppConfig:
    """Provide user-configurable weather dashboard defaults."""

    SECRETS_SECTION: str = "weather_dashboard"
    DEFAULT_CITY: str = "Budapest, Hungary"
    DEFAULT_FORECAST_DAYS: int = 5
    DEFAULT_TIMEZONE: str = "auto"
    DEFAULT_GEOCODING_RESULT_COUNT: int = 10
    DEFAULT_MIN_SEARCH_TERM_LENGTH: int = 3

    def __init__(self) -> None:
        """Initialize app-level settings from Streamlit secrets."""
        self._default_city: str = str(
            self._get_secret_value("default_city", self.DEFAULT_CITY)
        )
        self._forecast_days: int = self._get_positive_int_secret(
            "forecast_days",
            self.DEFAULT_FORECAST_DAYS,
        )
        self._timezone: str = str(
            self._get_secret_value("timezone", self.DEFAULT_TIMEZONE)
        )
        self._geocoding_result_count: int = self._get_positive_int_secret(
            "geocoding_result_count",
            self.DEFAULT_GEOCODING_RESULT_COUNT,
        )
        self._min_search_term_length: int = self._get_positive_int_secret(
            "min_search_term_length",
            self.DEFAULT_MIN_SEARCH_TERM_LENGTH,
        )

    @classmethod
    def _get_weather_dashboard_secrets(cls) -> dict[str, object]:
        """Return the weather dashboard secrets section if it exists."""
        try:
            secrets: object = st.secrets.get(cls.SECRETS_SECTION, {})
        except Exception:
            return {}

        if isinstance(secrets, Mapping):
            typed_secrets = cast(Mapping[object, object], secrets)
            return {
                str(key): value for key, value in typed_secrets.items()
            }

        return {}

    @classmethod
    def _get_secret_value(
        cls,
        key: str,
        default_value: object,
    ) -> object:
        """Return one weather dashboard secret value."""
        return cls._get_weather_dashboard_secrets().get(key, default_value)

    @classmethod
    def _get_positive_int_secret(cls, key: str, default_value: int) -> int:
        """Return one secret value as a positive integer."""
        value: object = cls._get_secret_value(key, default_value)
        parsed_value: int

        if isinstance(value, int):
            parsed_value = value
        elif isinstance(value, str):
            try:
                parsed_value = int(value)
            except ValueError as error:
                raise ValueError(f"{key} must be an integer.") from error
        else:
            raise ValueError(f"{key} must be an integer.")

        if parsed_value < 1:
            raise ValueError(f"{key} must be greater than 0.")

        return parsed_value

    def get_default_city(self) -> str:
        """Return the configured default city."""
        return self._default_city

    def get_forecast_days(self) -> int:
        """Return the configured forecast day count."""
        return self._forecast_days

    def get_timezone(self) -> str:
        """Return the configured forecast timezone."""
        return self._timezone

    def get_geocoding_result_count(self) -> int:
        """Return the configured geocoding result count."""
        return self._geocoding_result_count

    def get_min_search_term_length(self) -> int:
        """Return the configured minimum autocomplete search length."""
        return self._min_search_term_length

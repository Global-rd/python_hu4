"""
Application-level configuration for the weather dashboard.
"""

from collections.abc import Mapping
from typing import cast

import streamlit as st


class WeatherDashboardAppConfig:
    """Provide user-configurable weather dashboard defaults."""

    SECRETS_SECTION: str = "weather_dashboard"
    DEFAULT_CITY: str = "Budapest"
    DEFAULT_FORECAST_DAYS: int = 5
    DEFAULT_TIMEZONE: str = "auto"

    def __init__(self) -> None:
        """Initialize app-level settings from Streamlit secrets."""
        self._default_city: str = str(
            self._get_secret_value("default_city", self.DEFAULT_CITY)
        )
        self._forecast_days: int = self._parse_forecast_days(
            self._get_secret_value(
                "forecast_days",
                self.DEFAULT_FORECAST_DAYS,
            )
        )
        self._timezone: str = str(
            self._get_secret_value("timezone", self.DEFAULT_TIMEZONE)
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

    @staticmethod
    def _parse_forecast_days(value: object) -> int:
        """Return forecast_days as a positive integer."""
        try:
            forecast_days = int(value)
        except (TypeError, ValueError) as error:
            raise ValueError("forecast_days must be an integer.") from error

        if forecast_days < 1:
            raise ValueError("forecast_days must be greater than 0.")

        return forecast_days

    def get_default_city(self) -> str:
        """Return the configured default city."""
        return self._default_city

    def get_forecast_days(self) -> int:
        """Return the configured forecast day count."""
        return self._forecast_days

    def get_timezone(self) -> str:
        """Return the configured forecast timezone."""
        return self._timezone

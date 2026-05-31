"""
Streamlit session state helper for the weather dashboard.
"""

import streamlit as st


class WeatherDashboardState:
    """Manage Streamlit session state for dashboard filters."""

    SEARCHED_CITY_STATE_KEY: str = "weather_dashboard_searched_city"
    CITY_INPUT_STATE_KEY: str = "weather_dashboard_city_input"

    def __init__(self, default_city: str) -> None:
        """Initialize dashboard state with the configured default city."""
        self.default_city: str = default_city

        if self.CITY_INPUT_STATE_KEY not in st.session_state:
            st.session_state[self.CITY_INPUT_STATE_KEY] = default_city

        if self.SEARCHED_CITY_STATE_KEY not in st.session_state:
            st.session_state[self.SEARCHED_CITY_STATE_KEY] = default_city

    def get_searched_city(self) -> str:
        """Return the currently selected searched city."""
        return str(st.session_state[self.SEARCHED_CITY_STATE_KEY])

    def set_searched_city(self, city_name: str) -> None:
        """Store the currently selected searched city."""
        st.session_state[self.SEARCHED_CITY_STATE_KEY] = city_name

    def get_city_input(self) -> str:
        """Return the current city input value."""
        return str(st.session_state[self.CITY_INPUT_STATE_KEY])

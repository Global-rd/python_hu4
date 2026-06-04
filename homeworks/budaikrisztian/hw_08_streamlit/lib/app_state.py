"""
Streamlit session state helper for the weather dashboard.
"""

from typing import cast

import streamlit as st

from .app_types import DashboardLocation


class AppState:
    """Manage Streamlit session state for dashboard filters."""

    SELECTED_LOCATION_STATE_KEY: str = "weather_dashboard_selected_location"
    APPLIED_LOCATION_STATE_KEY: str = "weather_dashboard_applied_location"
    SEARCH_LOG_PENDING_STATE_KEY: str = (
        "weather_dashboard_search_log_pending"
    )

    def __init__(self) -> None:
        """Initialize dashboard location state."""
        if self.SELECTED_LOCATION_STATE_KEY not in st.session_state:
            st.session_state[self.SELECTED_LOCATION_STATE_KEY] = None

        if self.APPLIED_LOCATION_STATE_KEY not in st.session_state:
            st.session_state[self.APPLIED_LOCATION_STATE_KEY] = None

        if self.SEARCH_LOG_PENDING_STATE_KEY not in st.session_state:
            st.session_state[self.SEARCH_LOG_PENDING_STATE_KEY] = False

    def set_selected_location(
        self,
        location: DashboardLocation | None,
    ) -> None:
        """Store the currently selected autocomplete location."""
        st.session_state[self.SELECTED_LOCATION_STATE_KEY] = location

    def get_selected_location(self) -> DashboardLocation | None:
        """Return the currently selected autocomplete location."""
        selected_location: object = st.session_state[
            self.SELECTED_LOCATION_STATE_KEY
        ]

        if selected_location is None:
            return None

        return cast(DashboardLocation, selected_location)

    def set_initial_location(self, location: DashboardLocation) -> None:
        """Store the default location without treating it as a search."""
        st.session_state[self.SELECTED_LOCATION_STATE_KEY] = location
        st.session_state[self.APPLIED_LOCATION_STATE_KEY] = location
        st.session_state[self.SEARCH_LOG_PENDING_STATE_KEY] = False

    def apply_selected_location(self) -> None:
        """Use the selected autocomplete location as the active location."""
        st.session_state[self.APPLIED_LOCATION_STATE_KEY] = (
            self.get_selected_location()
        )
        st.session_state[self.SEARCH_LOG_PENDING_STATE_KEY] = True

    def get_applied_location(self) -> DashboardLocation | None:
        """Return the active location used by the dashboard."""
        applied_location: object = st.session_state[
            self.APPLIED_LOCATION_STATE_KEY
        ]

        if applied_location is None:
            return None

        return cast(DashboardLocation, applied_location)

    def should_log_applied_location(self) -> bool:
        """Return whether the current applied location needs logging."""
        return bool(
            st.session_state[self.SEARCH_LOG_PENDING_STATE_KEY]
        )

    def mark_applied_location_logged(self) -> None:
        """Mark the current applied location as logged."""
        st.session_state[self.SEARCH_LOG_PENDING_STATE_KEY] = False

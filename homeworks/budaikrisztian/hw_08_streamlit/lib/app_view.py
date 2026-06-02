"""
Streamlit app-level view coordinator for the weather dashboard.
"""

from collections.abc import Callable

import streamlit as st

from .app_state import AppState
from .app_types import DashboardLocation
from .open_meteo import ForecastData
from .view import ContentView, SidebarFilterView


class AppView:
    """Coordinate Streamlit UI elements for the weather dashboard."""

    DEFAULT_PAGE_ICON: str = "🌦️"

    def __init__(
        self,
        default_city: str,
        forecast_days: int,
        min_search_term_length: int,
    ) -> None:
        """Initialize the view with its default filter state."""
        self.default_city: str = default_city
        self.forecast_days: int = forecast_days
        self.min_search_term_length: int = min_search_term_length
        self.state: AppState = AppState()
        self.sidebar_filter_view: SidebarFilterView = (
            SidebarFilterView(
                self.state,
                min_search_term_length,
            )
        )
        self.dashboard_content_view: ContentView = (
            ContentView(forecast_days)
        )
        self.page_icon: str = self.DEFAULT_PAGE_ICON
        self._configure_page()

    def _configure_page(self) -> None:
        """Configure the Streamlit page."""
        st.set_page_config(
            page_title="City Weather App",
            page_icon=self.page_icon,
            layout="centered",
        )

    @staticmethod
    def _get_display_city(location: DashboardLocation) -> str:
        """Return a user-facing city and country label."""
        return f"{location['name']}, {location['country']}"

    @staticmethod
    def _render_styles() -> None:
        """Apply local Streamlit styling for the homework dashboard."""
        st.markdown(
            """
            <style>
                .sidebar-filter-title {
                    align-items: center;
                    display: flex;
                    gap: 0.5rem;
                    margin-bottom: 0.75rem;
                }

                .sidebar-filter-title img {
                    display: block;
                    height: 34px;
                    width: 34px;
                }

                .sidebar-filter-title span {
                    color: #f4f4f5;
                    font-size: 1.15rem;
                    font-weight: 700;
                    line-height: 1;
                    margin: 0;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    def _render_header(self) -> None:
        """Render the dashboard title."""
        st.title(
            f"{self.page_icon}"
            "City Weather Map & Data Visualization App"
        )

    def _render_sidebar_filter(
        self,
        search_locations: Callable[[str], list[DashboardLocation]],
    ) -> DashboardLocation | None:
        """Render sidebar city filter controls and return active location."""
        return self.sidebar_filter_view.render(search_locations)

    def render_layout(
        self,
        search_locations: Callable[[str], list[DashboardLocation]],
    ) -> DashboardLocation | None:
        """Render static layout elements and return the active location."""
        self._render_styles()
        self._render_header()

        return self._render_sidebar_filter(search_locations)

    def set_initial_location(self, location: DashboardLocation) -> None:
        """Store the default location used on first page load."""
        self.state.set_initial_location(location)

    def get_applied_location(self) -> DashboardLocation | None:
        """Return the currently active dashboard location."""
        return self.state.get_applied_location()

    def should_log_applied_location(self) -> bool:
        """Return whether the active location should be logged."""
        return self.state.should_log_applied_location()

    def mark_applied_location_logged(self) -> None:
        """Mark the active location search as logged."""
        self.state.mark_applied_location_logged()

    @staticmethod
    def render_warning(message: str) -> None:
        """Render a user-facing warning message."""
        st.warning(message)

    def render_dashboard(
        self,
        location: DashboardLocation,
        forecast: ForecastData,
    ) -> None:
        """Render current weather, map and forecast chart."""
        self.dashboard_content_view.render(location, forecast)

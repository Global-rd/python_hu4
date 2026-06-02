"""
Sidebar filter view component for the weather dashboard.
"""

import base64
from collections.abc import Callable
from pathlib import Path
from typing import cast

import streamlit as st
from streamlit_searchbox import st_searchbox  # type: ignore[import-untyped]

from ..app_state import AppState
from ..app_types import (
    DashboardLocation,
    LocationSearchOption,
)


class SidebarFilterView:
    """Render sidebar autocomplete city filter controls."""

    def __init__(
        self,
        state: AppState,
        min_search_term_length: int,
    ) -> None:
        """Initialize the sidebar filter view."""
        self.state: AppState = state
        self.min_search_term_length: int = min_search_term_length
        self.filter_icon_path: Path = (
            Path(__file__).parent.parent.parent / "assets/filter_icon.svg"
        )

    @staticmethod
    def _get_image_data_uri(image_path: Path, media_type: str) -> str:
        """Return an image file as an embeddable data URI."""
        image_data: str = base64.b64encode(
            image_path.read_bytes()
        ).decode("ascii")

        return f"data:{media_type};base64,{image_data}"

    @staticmethod
    def _get_location_option_label(location: DashboardLocation) -> str:
        """Return a clear autocomplete label for one location."""
        return location["label"]

    @classmethod
    def _create_location_search_option(
        cls,
        location: DashboardLocation,
    ) -> LocationSearchOption:
        """Convert a dashboard location to a searchbox option."""
        return (
            cls._get_location_option_label(location),
            location,
        )

    def _render_title(self) -> None:
        """Render the sidebar filter title."""
        filter_icon_data_uri: str = self._get_image_data_uri(
            self.filter_icon_path,
            "image/svg+xml",
        )

        st.markdown(
            f"""
            <div class="sidebar-filter-title">
                <img
                    src="{filter_icon_data_uri}"
                    alt="Filter icon"
                />
                <span>Filter</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def _create_default_options(
        self,
        selected_location: DashboardLocation | None,
    ) -> tuple[str, list[LocationSearchOption] | None]:
        """Return the searchbox default term and options."""
        if selected_location is None:
            return "", None

        default_option: LocationSearchOption = (
            self._create_location_search_option(selected_location)
        )

        return default_option[0], [default_option]

    def render(
        self,
        search_locations: Callable[[str], list[DashboardLocation]],
    ) -> DashboardLocation | None:
        """Render sidebar city filter controls and return active location."""
        selected_location: DashboardLocation | None = (
            self.state.get_selected_location()
        )
        default_searchterm: str
        default_options: list[LocationSearchOption] | None
        default_searchterm, default_options = self._create_default_options(
            selected_location
        )

        def search_location_options(
            search_term: str,
        ) -> list[LocationSearchOption]:
            return [
                self._create_location_search_option(location)
                for location in search_locations(search_term)
            ]

        with st.sidebar:
            self._render_title()
            searchbox_value: object = st_searchbox(
                search_location_options,
                key="weather_dashboard_location_searchbox_v3",
                label="City",
                placeholder=(
                    "Type at least "
                    f"{self.min_search_term_length} characters..."
                ),
                default=selected_location,
                default_searchterm=default_searchterm,
                default_options=default_options,
                edit_after_submit="option",
            )

            if searchbox_value is not None:
                self.state.set_selected_location(
                    cast(DashboardLocation, searchbox_value)
                )

            if st.button("Apply", type="primary"):
                if self.state.get_selected_location() is None:
                    st.warning("Choose a city first.")
                else:
                    self.state.apply_selected_location()

        return self.state.get_applied_location()

"""
Streamlit view layer for the weather dashboard.
"""

import base64
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

from .open_meteo import CityLocation, ForecastData
from .weather_dashboard_state import WeatherDashboardState


class WeatherDashboardView:
    """Render Streamlit UI elements for the weather dashboard."""

    DEFAULT_PAGE_ICON: str = "🌦️"

    def __init__(self, default_city: str, forecast_days: int) -> None:
        """Initialize the view with its default filter state."""
        self.default_city: str = default_city
        self.forecast_days: int = forecast_days
        self.state: WeatherDashboardState = WeatherDashboardState(default_city)
        self.page_icon: str = self.DEFAULT_PAGE_ICON
        self.filter_icon_path: Path = (
            Path(__file__).parent.parent / "assets/filter_icon.svg"
        )
        self._configure_page()

    def _configure_page(self) -> None:
        """Configure the Streamlit page."""
        st.set_page_config(
            page_title="City Weather App",
            page_icon=self.page_icon,
            layout="centered",
        )

    @staticmethod
    def _get_display_city(location: CityLocation) -> str:
        """Return a user-facing city and country label."""
        return f"{location['name']}, {location['country']}"

    @staticmethod
    def _create_forecast_df(forecast: ForecastData) -> pd.DataFrame:
        """Return hourly forecast data as a dataframe."""
        hourly = forecast["hourly"]

        return pd.DataFrame(
            {
                "time": pd.to_datetime(hourly["time"]),
                "temperature": hourly["temperature_2m"],
            }
        )

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

    @staticmethod
    def _get_image_data_uri(image_path: Path, media_type: str) -> str:
        """Return an image file as an embeddable data URI."""
        image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

        return f"data:{media_type};base64,{image_data}"

    def _render_sidebar_filter(self) -> str:
        """Render sidebar city filter controls and return selected city."""
        filter_icon_data_uri = self._get_image_data_uri(
            self.filter_icon_path,
            "image/svg+xml",
        )

        with st.sidebar:
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
            with st.form(
                "weather_dashboard_filter_form",
                enter_to_submit=False,
            ):
                st.text_input(
                    "City",
                    key=self.state.CITY_INPUT_STATE_KEY,
                )

                if st.form_submit_button("Apply", type="primary"):
                    self.state.set_searched_city(
                        self.state.get_city_input()
                    )

        return self.state.get_searched_city()

    def render_layout(self) -> str:
        """Render static layout elements and return the selected city."""
        self._render_styles()
        self._render_header()

        return self._render_sidebar_filter()

    @staticmethod
    def render_warning(message: str) -> None:
        """Render a user-facing warning message."""
        st.warning(message)

    @staticmethod
    def _render_map(location: CityLocation) -> None:
        """Render the city location on a map."""
        location_df = pd.DataFrame(
            [
                {
                    "lat": location["latitude"],
                    "lon": location["longitude"],
                }
            ]
        )
        st.map(location_df, latitude="lat", longitude="lon", zoom=11)

    @staticmethod
    def _render_temperature_chart(
        forecast_df: pd.DataFrame,
        chart_key: str,
    ) -> None:
        """Render the hourly temperature line chart."""
        chart_df = forecast_df.copy()
        chart_df["time"] = chart_df["time"].dt.strftime("%m.%d %H:%M")
        chart_fingerprint = (
            f"{chart_df['temperature'].iloc[0]:.1f}_"
            f"{chart_df['temperature'].max():.1f}_"
            f"{chart_df['temperature'].min():.1f}_"
            f"{chart_df['temperature'].sum():.1f}"
        )

        chart = (
            alt.Chart(chart_df)
            .mark_line(color="#7cc7ff", strokeWidth=2)
            .encode(
                x=alt.X(
                    "time:O",
                    title=None,
                    axis=alt.Axis(
                        labelAngle=-90,
                        labelColor="#f4f4f5",
                        labelFontSize=10,
                        labelOverlap=True,
                        tickColor="#3b414b",
                        domainColor="#3b414b",
                    ),
                ),
                y=alt.Y(
                    "temperature:Q",
                    title=None,
                    scale=alt.Scale(zero=True),
                    axis=alt.Axis(
                        grid=True,
                        gridColor="#303640",
                        labelColor="#f4f4f5",
                        labelFontSize=10,
                        tickColor="#3b414b",
                        domainColor="#3b414b",
                    ),
                ),
            )
            .properties(height=300, background="#171b22")
        )

        st.altair_chart(
            chart,
            width="stretch",
            key=f"{chart_key}_{chart_fingerprint}",
            theme=None,
        )

    def render_dashboard(
        self,
        location: CityLocation,
        forecast: ForecastData,
    ) -> None:
        """Render current weather, map and forecast chart."""
        current = forecast["current"]
        display_city = self._get_display_city(location)

        st.subheader(f"Current Weather in {display_city}")
        metric_columns = st.columns(3)
        metric_columns[0].metric(
            "Temperature (C)",
            f"{current['temperature_2m']:.1f}°C",
        )
        metric_columns[1].metric(
            "Humidity (%)",
            f"{current['relative_humidity_2m']}%",
        )
        metric_columns[2].metric(
            "Wind Speed (km/h)",
            f"{current['wind_speed_10m']:.1f} km/h",
        )

        st.subheader("Map")
        self._render_map(location)

        st.subheader(
            f"Hourly Temperature Forecast (Next {self.forecast_days} Days)"
        )
        self._render_temperature_chart(
            self._create_forecast_df(forecast),
            f"temperature_chart_{location['id']}",
        )

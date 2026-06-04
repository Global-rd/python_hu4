"""
Dashboard content view component for the weather dashboard.
"""

import altair as alt
import pandas as pd  # type: ignore[import-untyped]
import streamlit as st

from ..app_types import DashboardLocation
from ..open_meteo import ForecastData
from ..open_meteo.types import CurrentWeather


class ContentView:
    """Render current weather, map and forecast chart."""

    def __init__(self, forecast_days: int) -> None:
        """Initialize dashboard content view."""
        self.forecast_days: int = forecast_days

    @staticmethod
    def _get_display_city(location: DashboardLocation) -> str:
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
    def _render_map(location: DashboardLocation) -> None:
        """Render the city location on a map."""
        location_df: pd.DataFrame = pd.DataFrame(
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
        chart_df: pd.DataFrame = forecast_df.copy()
        chart_df["time"] = chart_df["time"].dt.strftime("%m.%d %H:%M")
        chart_fingerprint: str = (
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

    def render(
        self,
        location: DashboardLocation,
        forecast: ForecastData,
    ) -> None:
        """Render current weather, map and forecast chart."""
        current: CurrentWeather = forecast["current"]
        display_city: str = self._get_display_city(location)

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

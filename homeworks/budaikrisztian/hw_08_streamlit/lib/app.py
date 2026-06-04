"""
Streamlit weather map and data visualization application.
"""

from .app_config import AppConfig
from .app_types import DashboardLocation
from .app_view import AppView
from .open_meteo import ForecastData
from .open_meteo.types import CurrentWeather
from .search_logger import SearchLogger
from .service import ForecastService, LocationSearchService


class App:
    """Coordinate weather API calls, logging and dashboard rendering."""

    def __init__(self, app_config: AppConfig) -> None:
        """Initialize the dashboard dependencies."""
        self.app_config: AppConfig = app_config
        self.location_search_service: LocationSearchService = (
            LocationSearchService(
                app_config.get_geocoding_result_count(),
                app_config.get_min_search_term_length(),
            )
        )
        self.forecast_service: ForecastService = (
            ForecastService(
                app_config.get_forecast_days(),
                app_config.get_timezone(),
            )
        )
        self.search_logger: SearchLogger = SearchLogger()
        self.view: AppView = AppView(
            app_config.get_default_city(),
            app_config.get_forecast_days(),
            app_config.get_min_search_term_length(),
        )

    @staticmethod
    def _get_display_city(location: DashboardLocation) -> str:
        """Return a user-facing city and country label."""
        return f"{location['name']}, {location['country']}"

    def _initialize_default_location(self) -> None:
        """Load the configured default location on first page load."""
        if self.view.get_applied_location() is not None:
            return

        location: DashboardLocation = (
            self.location_search_service.get_default_location(
                self.app_config.get_default_city()
            )
        )
        self.view.set_initial_location(location)

    def log_search(
        self,
        location: DashboardLocation,
        forecast: ForecastData,
    ) -> None:
        """Log one successful weather dashboard search."""
        current: CurrentWeather = forecast["current"]
        self.search_logger.log_search(
            self._get_display_city(location),
            current["temperature_2m"],
            current["relative_humidity_2m"],
            current["wind_speed_10m"],
        )

    def run(self) -> None:
        """Run the Streamlit weather dashboard."""
        try:
            self._initialize_default_location()
            location: DashboardLocation | None = self.view.render_layout(
                self.location_search_service.search_locations
            )

            if location is None:
                self.view.render_warning("Choose a city first.")
                return

            forecast: ForecastData = self.forecast_service.get_forecast(
                location
            )
            self.view.render_dashboard(location, forecast)

            if self.view.should_log_applied_location():
                self.log_search(location, forecast)
                self.view.mark_applied_location_logged()
        except (RuntimeError, ValueError) as error:
            self.view.render_warning(str(error))

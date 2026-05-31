"""
SQLite logger for weather dashboard searches.
"""

import sqlite3
from datetime import datetime
from pathlib import Path


class SearchLogger:
    """Store weather searches in a local SQLite database."""

    TABLE_NAME: str = "weather_searches"

    def __init__(
        self,
        db_path: Path | None = None,
    ) -> None:
        """Initialize the logger database path and schema."""
        self.db_path: Path = (
            db_path
            or Path(__file__).parent.parent / "weather_searches.sqlite3"
        )
        self.create_table()

    def create_table(self) -> None:
        """Create the searches table if it does not exist yet."""
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city_name TEXT NOT NULL,
                    temperature REAL NOT NULL,
                    humidity INTEGER NOT NULL,
                    wind_speed REAL NOT NULL,
                    searched_at TEXT NOT NULL
                )
                """
            )

    def log_search(
        self,
        city_name: str,
        temperature: float,
        humidity: int,
        wind_speed: float,
    ) -> None:
        """Insert one weather search record into the database."""
        with sqlite3.connect(self.db_path) as connection:
            connection.execute(
                f"""
                INSERT INTO {self.TABLE_NAME} (
                    city_name,
                    temperature,
                    humidity,
                    wind_speed,
                    searched_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    city_name,
                    temperature,
                    humidity,
                    wind_speed,
                    datetime.now().isoformat(timespec="seconds"),
                ),
            )

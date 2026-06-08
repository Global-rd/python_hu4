"""
Runtime configuration loaded from environment variables.
"""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    """Application configuration values."""

    output_path: Path
    headless: bool
    max_workers: int

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Load configuration from .env and environment variables."""
        load_dotenv()

        return cls(
            output_path=Path(os.getenv("OUTPUT_PATH", "output/quotes.csv")),
            headless=cls._parse_bool(os.getenv("HEADLESS", "true")),
            max_workers=cls._parse_positive_int(
                os.getenv("MAX_WORKERS", "3")
            ),
        )

    @staticmethod
    def _parse_bool(value: str) -> bool:
        """Parse common environment-style boolean values."""
        return value.strip().lower() in {"1", "true", "yes", "on"}

    @staticmethod
    def _parse_positive_int(value: str) -> int:
        """Parse a positive integer environment value."""
        parsed_value: int = int(value)

        if parsed_value < 1:
            raise ValueError("MAX_WORKERS must be at least 1.")

        return parsed_value

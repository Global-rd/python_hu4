"""
Homework 8: Streamlit weather map and data visualization app.
Author: Budai Krisztian
"""

from lib.app import App
from lib.app_config import AppConfig

if __name__ == "__main__":
    app_config = AppConfig()

    App(app_config).run()

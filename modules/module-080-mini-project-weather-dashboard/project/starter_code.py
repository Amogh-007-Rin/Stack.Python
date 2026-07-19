"""
Weather Dashboard CLI - Starter Code

TODO: Implement each function following the type hints and docstrings.
"""

import json
from typing import Any, Dict, List, Optional

import requests


# TODO: Implement this function
def build_url(city: str, api_key: str) -> str:
    """Construct the OpenWeatherMap current weather URL.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        Full URL string for the API request.
    """
    pass


# TODO: Implement this function
def fetch_current_weather(city: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Fetch current weather data from OpenWeatherMap.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        Parsed JSON response dict, or None on failure.
    """
    pass


# TODO: Implement this function
def parse_current_weather(data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract relevant fields from the raw API response.

    Args:
        data: Raw JSON response from OpenWeatherMap.

    Returns:
        Dictionary with keys: city, temperature, humidity, conditions, wind_speed.
    """
    pass


# TODO: Implement this function
def display_weather(weather: Dict[str, Any]) -> None:
    """Print a formatted weather report to the console.

    Args:
        weather: Dictionary with parsed weather data.
    """
    pass


# TODO: Implement this function
def save_search(city: str, filepath: str, max_searches: int = 5) -> None:
    """Save a city to the recent searches JSON file.

    Args:
        city: City name to save.
        filepath: Path to the JSON file.
        max_searches: Maximum number of recent searches to keep.
    """
    pass


# TODO: Implement this function
def load_recent_searches(filepath: str) -> List[str]:
    """Load recent searches from the JSON file.

    Args:
        filepath: Path to the JSON file.

    Returns:
        List of recent city names, or empty list if file doesn't exist.
    """
    pass


# TODO: Implement this function
def fetch_forecast(city: str, api_key: str) -> Optional[List[Dict[str, Any]]]:
    """Fetch the 5-day weather forecast.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        List of parsed forecast entries, or None on failure.
    """
    pass


# TODO: Implement this function
def display_forecast(forecasts: List[Dict[str, Any]]) -> None:
    """Print the 5-day forecast to the console.

    Args:
        forecasts: List of parsed forecast entries (datetime, temperature, conditions).
    """
    pass


# TODO: Implement the CLI entry point
def main() -> None:
    """Run the Weather Dashboard CLI using command-line arguments."""
    pass


if __name__ == "__main__":
    main()

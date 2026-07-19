"""
Solutions for Weather Dashboard CLI exercises.

Google-style docstrings and complete type hints throughout.
"""

import json
import sys
from typing import Any, Dict, List, Optional

import requests


# ---------------------------------------------------------------------------
# Exercise 1: API Setup
# ---------------------------------------------------------------------------

def build_url(city: str, api_key: str) -> str:
    """Construct the OpenWeatherMap current weather URL.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        Full URL string for the API request.
    """
    base: str = "https://api.openweathermap.org/data/2.5/weather"
    return f"{base}?q={city}&appid={api_key}&units=metric"


def build_forecast_url(city: str, api_key: str) -> str:
    """Construct the OpenWeatherMap 5-day forecast URL.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        Full URL string for the forecast API request.
    """
    base: str = "https://api.openweathermap.org/data/2.5/forecast"
    return f"{base}?q={city}&appid={api_key}&units=metric"


# ---------------------------------------------------------------------------
# Exercise 2: Fetch Current Weather
# ---------------------------------------------------------------------------

def fetch_current_weather(city: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Fetch current weather data from OpenWeatherMap.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        Parsed JSON response dict, or None on failure.
    """
    url: str = build_url(city, api_key)
    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


# ---------------------------------------------------------------------------
# Exercise 3: Parse Weather Data
# ---------------------------------------------------------------------------

def parse_current_weather(data: Dict[str, Any]) -> Dict[str, Any]:
    """Extract relevant fields from the raw API response.

    Args:
        data: Raw JSON response from OpenWeatherMap current weather endpoint.

    Returns:
        Dictionary with keys: city, temperature, humidity, conditions, wind_speed.
    """
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "conditions": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
    }


# ---------------------------------------------------------------------------
# Exercise 4: Display Weather
# ---------------------------------------------------------------------------

def display_weather(weather: Dict[str, Any]) -> None:
    """Print a formatted weather report to the console.

    Args:
        weather: Dictionary with parsed weather data.
    """
    print("\n" + "=" * 40)
    print(f"  Weather in {weather['city']}")
    print("=" * 40)
    print(f"  Temperature: {weather['temperature']:.1f}°C")
    print(f"  Humidity:    {weather['humidity']}%")
    print(f"  Conditions:  {weather['conditions'].capitalize()}")
    print(f"  Wind Speed:  {weather['wind_speed']} m/s")
    print("=" * 40 + "\n")


# ---------------------------------------------------------------------------
# Exercise 5: Error Handling
# ---------------------------------------------------------------------------

def safe_fetch_weather(city: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Fetch weather with comprehensive error handling and user feedback.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        Parsed weather dict, or None if any error occurred.
    """
    url: str = build_url(city, api_key)
    try:
        response: requests.Response = requests.get(url, timeout=10)
        if response.status_code == 404:
            print(f"Error: City '{city}' not found.")
            return None
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your credentials.")
            return None
        response.raise_for_status()
        return parse_current_weather(response.json())
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None


# ---------------------------------------------------------------------------
# Exercise 6: Store Recent Searches
# ---------------------------------------------------------------------------

def save_search(city: str, filepath: str, max_searches: int = 5) -> None:
    """Save a city to the recent searches file.

    Args:
        city: City name to save.
        filepath: Path to the JSON file storing recent searches.
        max_searches: Maximum number of recent searches to keep.
    """
    searches: List[str] = load_recent_searches(filepath)
    if city in searches:
        searches.remove(city)
    searches.insert(0, city)
    searches = searches[:max_searches]
    with open(filepath, "w") as f:
        json.dump(searches, f)


def load_recent_searches(filepath: str) -> List[str]:
    """Load recent searches from the JSON file.

    Args:
        filepath: Path to the JSON file.

    Returns:
        List of recent city names, or empty list if file doesn't exist.
    """
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def display_recent_searches(filepath: str) -> None:
    """Print recent searches to the console.

    Args:
        filepath: Path to the JSON file.
    """
    searches: List[str] = load_recent_searches(filepath)
    if searches:
        print("Recent searches:")
        for i, city in enumerate(searches, 1):
            print(f"  {i}. {city}")
    else:
        print("No recent searches.")


# ---------------------------------------------------------------------------
# Exercise 7: 5-Day Forecast
# ---------------------------------------------------------------------------

def fetch_forecast(city: str, api_key: str) -> Optional[List[Dict[str, Any]]]:
    """Fetch the 5-day weather forecast.

    Args:
        city: City name to query.
        api_key: OpenWeatherMap API key.

    Returns:
        List of parsed forecast entries, or None on failure.
    """
    url: str = build_forecast_url(city, api_key)
    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
        forecasts: List[Dict[str, Any]] = []
        for entry in data["list"]:
            forecasts.append({
                "datetime": entry["dt_txt"],
                "temperature": entry["main"]["temp"],
                "conditions": entry["weather"][0]["description"],
            })
        return forecasts
    except requests.exceptions.RequestException:
        return None


def display_forecast(forecasts: List[Dict[str, Any]]) -> None:
    """Print the 5-day forecast to the console.

    Args:
        forecasts: List of parsed forecast entries.
    """
    print("\n" + "-" * 50)
    print("  5-Day Forecast (3-hour intervals)")
    print("-" * 50)
    for f in forecasts[:8]:  # Show first 24 hours for brevity
        print(f"  {f['datetime']} | {f['temperature']:.1f}°C | {f['conditions'].capitalize()}")
    print("-" * 50 + "\n")


# ---------------------------------------------------------------------------
# Challenge: Full CLI
# ---------------------------------------------------------------------------

def main() -> None:
    """Run the Weather Dashboard CLI using command-line arguments."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Weather Dashboard CLI - Fetch current weather and 5-day forecast."
    )
    parser.add_argument("city", nargs="?", help="City name to query")
    parser.add_argument(
        "--api-key",
        help="OpenWeatherMap API key (defaults to environment variable OWM_API_KEY)",
        default=None,
    )
    parser.add_argument(
        "--forecast",
        action="store_true",
        help="Show 5-day forecast",
    )
    parser.add_argument(
        "--recent",
        action="store_true",
        help="Show recent searches",
    )
    parser.add_argument(
        "--history-file",
        default="recent_searches.json",
        help="Path to recent searches file",
    )

    args: argparse.Namespace = parser.parse_args()

    api_key: str = args.api_key or "YOUR_API_KEY_HERE"

    if args.recent:
        display_recent_searches(args.history_file)
        return

    if not args.city:
        parser.print_help()
        return

    # Fetch and display current weather
    weather: Optional[Dict[str, Any]] = safe_fetch_weather(args.city, api_key)
    if weather:
        display_weather(weather)
        save_search(args.city, args.history_file)

    # Fetch and display forecast
    if args.forecast:
        forecasts: Optional[List[Dict[str, Any]]] = fetch_forecast(args.city, api_key)
        if forecasts:
            display_forecast(forecasts)


if __name__ == "__main__":
    main()

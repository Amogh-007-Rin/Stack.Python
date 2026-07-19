# Exercises: Weather Dashboard CLI

These exercises guide you through building the weather dashboard step by step.

## Exercise 1: API Setup
Sign up for a free API key at OpenWeatherMap. Write a function `build_url(city: str, api_key: str) -> str` that constructs the API URL for current weather.

## Exercise 2: Fetch Current Weather
Write a function `fetch_current_weather(city: str, api_key: str) -> dict` that uses `requests.get()` to fetch current weather data. Return the JSON response.

## Exercise 3: Parse Weather Data
Write a function `parse_current_weather(data: dict) -> dict` that extracts: city name, temperature (in Celsius), humidity, conditions description, and wind speed.

## Exercise 4: Display Weather
Write a function `display_weather(weather: dict) -> None` that prints a nicely formatted weather report to the console.

## Exercise 5: Error Handling
Add error handling for:
- City not found (404)
- Invalid API key (401)
- Network errors and timeouts
- Display user-friendly messages for each case.

## Exercise 6: Store Recent Searches
Write functions `save_search(city: str, filepath: str) -> None` and `load_recent_searches(filepath: str) -> list` that store/retrieve city names in a JSON file (keep last 5).

## Exercise 7: 5-Day Forecast
Write functions to fetch and display a 5-day weather forecast (3-hour intervals) showing date, temperature range, and conditions.

## Challenge: Full CLI
Combine everything into a CLI that accepts city names as command-line arguments and displays current weather + forecast. Use `argparse` for command-line argument parsing.

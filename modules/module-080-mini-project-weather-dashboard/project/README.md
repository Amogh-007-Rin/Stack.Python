# Weather Dashboard CLI

A command-line weather dashboard that fetches current weather and 5-day forecasts from the OpenWeatherMap API.

## Features

- Fetch current weather by city name
- Display temperature, humidity, conditions, wind speed
- 5-day weather forecast (3-hour intervals)
- Store recent searches in a JSON file
- Comprehensive error handling

## Setup

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Set your API key as an environment variable:

```bash
export OWM_API_KEY="your_api_key_here"
```

## Usage

```bash
# Current weather
python weather_dashboard.py London

# With explicit API key
python weather_dashboard.py Tokyo --api-key YOUR_KEY

# 5-day forecast
python weather_dashboard.py Paris --forecast

# Show recent searches
python weather_dashboard.py --recent

# Custom history file
python weather_dashboard.py Berlin --history-file my_searches.json
```

## Starter Code

Open `starter_code.py` and follow the TODO comments to implement each function. The solution is in `solution/weather_dashboard.py`.

## Requirements

- Python 3.9+
- requests library

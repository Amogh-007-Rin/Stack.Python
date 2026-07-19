# Module 076: Working with APIs: the requests Library

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2 hours

## Learning Objectives

- Understand HTTP methods (GET, POST, PUT, DELETE) and status codes
- Make HTTP requests with the requests library
- Handle JSON responses
- Send query parameters and custom headers
- Authenticate with API keys and basic auth
- Handle HTTP errors gracefully

## Topics Covered

1. HTTP basics: methods and status codes
2. GET requests with requests.get()
3. POST, PUT, DELETE requests
4. Working with JSON responses
5. Query parameters and headers
6. Authentication (API keys, basic auth)
7. Error handling for HTTP errors

## Prerequisites

Modules 000-075.

## Key Concepts

```python
import requests

# GET request
response = requests.get('https://api.github.com/users/python')
if response.status_code == 200:
    data = response.json()
    print(data['login'])

# POST with JSON
response = requests.post(
    'https://api.example.com/data',
    json={'key': 'value'},
    headers={'Authorization': 'Bearer YOUR_TOKEN'}
)
```

## Resources

- requests documentation: https://requests.readthedocs.io
- HTTP Status Codes (MDN)
- JSONPlaceholder API for testing

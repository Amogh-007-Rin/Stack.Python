# Solutions: Working with APIs: requests

## Exercise 1: GET Request
```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()
print(data[0]['title'])
```

## Exercise 2: Query Parameters
```python
import requests

params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
posts = response.json()
print(f"Found {len(posts)} posts for user 1")
```

## Exercise 3: POST Request
```python
import requests

new_post = {
    'title': 'My New Post',
    'body': 'This is the content of the post.',
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print('Created post with ID:', response.json()['id'])
```

## Exercise 4: Error Handling
```python
import requests
from typing import Optional

def safe_fetch(url: str, timeout: int = 10) -> Optional[dict]:
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError):
        return None
```

## Exercise 5: Headers
```python
import requests

headers = {'User-Agent': 'MyApp/1.0'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json()['headers']['User-Agent'])
```

## Exercise 6: Authentication
```python
import requests
from typing import Optional

def fetch_protected(url: str, api_key: str) -> Optional[dict]:
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Test with httpbin
result = fetch_protected('https://httpbin.org/bearer', 'my-secret-token')
print(result)
```

## Challenge: API Client Class
```python
import requests
from typing import Optional, List, Dict

class GitHubClient:
    BASE_URL = 'https://api.github.com'

    def __init__(self, token: Optional[str] = None) -> None:
        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/vnd.github.v3+json'})
        if token:
            self.session.headers.update({'Authorization': f'token {token}'})

    def get_user(self, username: str) -> Optional[Dict]:
        url = f'{self.BASE_URL}/users/{username}'
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def get_repos(self, username: str) -> Optional[List[Dict]]:
        url = f'{self.BASE_URL}/users/{username}/repos'
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        return None

client = GitHubClient()
user = client.get_user('python')
print(user['login'] if user else 'Not found')
```

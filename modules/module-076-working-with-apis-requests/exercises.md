# Exercises: Working with APIs: requests

Use the JSONPlaceholder API (`https://jsonplaceholder.typicode.com`) for these exercises.

## Exercise 1: GET Request
Fetch all posts from `https://jsonplaceholder.typicode.com/posts` and print the title of the first post.

## Exercise 2: Query Parameters
Fetch posts by user ID 1 using query parameters. Print how many posts were returned.

## Exercise 3: POST Request
Create a new post by sending a POST request with title, body, and userId fields. Print the returned ID.

## Exercise 4: Error Handling
Write a function that safely fetches data from a URL. It should return the JSON data if successful, or None if the request fails. Handle timeout and connection errors.

## Exercise 5: Headers
Send a GET request with a custom `User-Agent` header and verify it was received by inspecting the response or using an echo service.

## Exercise 6: Authentication
Write a function that takes an API key and fetches data from a protected endpoint. (Use `httpbin.org/bearer` for testing.)

## Challenge: API Client Class
Create a `GitHubClient` class that wraps the GitHub API:
- `get_user(username: str) -> dict`
- `get_repos(username: str) -> list`
- Handle rate limiting (status 403) and authentication via token.

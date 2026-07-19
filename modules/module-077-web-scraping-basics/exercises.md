# Exercises: Web Scraping Basics: BeautifulSoup

Use the following HTML for exercises:

```python
html_content = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>My Heading</h1>
    <p class="intro">Welcome to the page.</p>
    <div id="main">
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
      <a href="https://example.com/1">Link 1</a>
      <a href="https://example.com/2">Link 2</a>
    </div>
    <p class="footer">Footer text</p>
  </body>
</html>
"""
```

## Exercise 1: Parse and Get Title
Parse the HTML and print the page title.

## Exercise 2: Find All Paragraphs
Find all `<p>` elements and print their text content.

## Exercise 3: Find by Class
Find the element with class `intro` and print its text.

## Exercise 4: Find by ID
Find the element with id `main` and print its tag name.

## Exercise 5: CSS Selectors
Use `.select()` with a CSS selector to find all list items and print their text.

## Exercise 6: Extract Links
Find all `<a>` tags and print their href attributes and text.

## Challenge: Real-World Scraping
Write a script that fetches `https://httpbin.org/html` (or a local HTML file), parses it, and extracts all headings, links, and paragraphs. Add a 1-second delay between requests.

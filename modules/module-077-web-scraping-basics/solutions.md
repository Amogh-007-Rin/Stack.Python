# Solutions: Web Scraping Basics: BeautifulSoup

## Exercises 1-6
```python
from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_content, 'lxml')

# Exercise 1: Title
print('Title:', soup.title.text)

# Exercise 2: All paragraphs
for p in soup.find_all('p'):
    print('Paragraph:', p.text)

# Exercise 3: Find by class
intro = soup.find(class_='intro')
print('Intro:', intro.text)

# Exercise 4: Find by id
main_div = soup.find(id='main')
print('Main tag:', main_div.name)

# Exercise 5: CSS selector
for li in soup.select('#main li'):
    print('List item:', li.text)

# Exercise 6: Links
for a in soup.find_all('a'):
    print(f"Link: {a.text} -> {a['href']}")
```

## Challenge: Real-World Scraping
```python
import requests
from bs4 import BeautifulSoup
import time

def scrape_page(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')

    print('Headings:')
    for h in soup.find_all(['h1', 'h2', 'h3']):
        print(f'  {h.name}: {h.text.strip()}')

    print('Links:')
    for a in soup.find_all('a', href=True):
        print(f'  {a.text.strip() or "N/A"}: {a["href"]}')

    print('Paragraphs:')
    for p in soup.find_all('p'):
        text = p.text.strip()
        if text:
            print(f'  {text[:100]}')

# Ethical: rate limiting
scrape_page('https://httpbin.org/html')
time.sleep(1)
```

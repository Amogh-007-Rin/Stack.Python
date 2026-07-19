# Module 077: Web Scraping Basics: BeautifulSoup

- **Phase:** 8. Data, Web & APIs
- **Duration:** 2 hours

## Learning Objectives

- Parse HTML with BeautifulSoup4 and lxml parser
- Find elements with .find(), .find_all(), and CSS selectors
- Navigate the parse tree
- Extract text content and attributes
- Understand ethical scraping practices

## Topics Covered

1. BeautifulSoup4 installation and setup
2. Parsing HTML documents
3. Finding elements (.find, .find_all)
4. CSS selectors (.select)
5. Navigating the parse tree
6. Extracting text and attributes
7. Ethical scraping: robots.txt, rate limiting

## Prerequisites

Modules 000-076.

## Key Concepts

```python
from bs4 import BeautifulSoup

html = '<html><body><h1>Title</h1><p class="content">Text</p></body></html>'
soup = BeautifulSoup(html, 'lxml')

title = soup.find('h1').text
paragraphs = soup.find_all('p')
content = soup.select('.content')
```

## Resources

- BeautifulSoup4 documentation
- lxml parser documentation
- robots.txt specification

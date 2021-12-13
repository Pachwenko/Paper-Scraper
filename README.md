# Paper Scraper

A little script I made to grab links to a bunch of images from unsplash because I didn't want to use the API. Outputs to a database file to be used for whatever purpose. Wouldn't recommend doing it this way, and this script is currently broken anyway.

Even though it's broken and you still want to use this you'll need to follow these steps:

- Download [the correct chrome webdriver](https://sites.google.com/chromium.org/driver/) and place it in the project folder
  - this should be named `chromedriver.exe`
- Install [poetry](https://python-poetry.org/) (python package management too)
- `poetry install`
- `poetry shell`
- `python main.py`

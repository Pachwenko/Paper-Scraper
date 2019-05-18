import urllib
import requests
import selenium
import bs4

"""
Steps of scraping our wallpaper database images:
1. Go to a url of collections, for example unsplash https://unsplash.com/collections/762960/dark-and-moody
2. Load the page with selenium, click the "load more images" button to load ALL images
3. Output to html and grab all the img links for full quality
4. Build a SQLITE Transaction
5. Repeat for a number of collections

For the future: 
 - Try new websites instead of only unsplash
 - Add static link to sql database and check version when app starts for new database, if new one then update it
 - Add automatic wallpaper changes with user-selected frequency
 - Only auto-grab images from user selected preferences (multiple)
 - - Make a separate SQLite database for user preferences and load them on startup
 - - If no preferences already then prompt user to set them (option to ignore this forever)
"""

"""
Helpful links:

 - https://pythonspot.com/selenium-click-button/
"""


class WallScraper:
    """
    What actually happens:

    1. Scrape 1 url, output img links to SQLite
    2. Continue until out of links
    """

    def __init__(self):
        pass

    def scrape(self):
        pass


def database_stats():
    pass


def main():
    scraper = WallScraper()
    scraper.scrape
    database_stats()


if __name__ == '__main__':
    main()



import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

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

def get_page_loaded():
    # Since this webpage has to load a shitload of images and have lots of javascript
    # we got to be careful with load times and selenium going real fast
    # How it works:
    # Load website
    # Find button to load all images
    # wait for page to load
    # scroll to the button
    # wait again for more stuff to load
    # scroll again and then click button

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get('https://unsplash.com/collections/762960/dark-and-moody')
    button = driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div[2]/button')

    time.sleep(2)

    driver.execute_script('window.scrollBy(659, 1393)')
    #
    # from selenium.webdriver.common.action_chains import ActionChains
    # ActionChains(driver).move_to_element(button).perform()
    time.sleep(2)
    driver.execute_script('window.scrollBy(659, 1393)')

    button.click()
    # button.click()

    return driver.page_source

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
    html = get_page_loaded()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())


if __name__ == '__main__':
    main()



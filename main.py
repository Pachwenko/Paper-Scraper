import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sqlite3
import datetime as dt

"""
Steps of scraping our wallpaper database images:
1. Go to a url of collections, for example unsplash https://unsplash.com/collections/762960/dark-and-moody
2. Load the page with selenium, click the "load more images" button to load ALL images
3. Output to html and grab all the image links for full quality
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
 - Unsplash anchor tags have class of _2Mc8_ just need to extract
    the href and prepend https://unsplash.com and then append /download?force=true to download it
"""

database_filepath = 'database.db'
# key represents the table name, value represents the actual url endpoint for that collection
# TODO: refactor this to support other websites than unsplash
collection_to_scrape = {'dark_and_moody': '/762960/dark-and-moody',
                        'background_textures': '/1368747/backgrounds-textures'}
bottom_page_y_pos = 175000
scroll_to_bottom = 'window.scrollBy(659, ' + str(bottom_page_y_pos) + ')'
base_url = 'https://unsplash.com'
collections_url = '/collections'
download_url = '/download?force=true'


class PaperScraper:
    """
    What actually happens:

    1. Scrape 1 url, output img links to SQLite
    2. Continue until out of links
    """

    def __init__(self):
        # create the database
        # use parse decltypes for python datetime objects, and insert as dt.datetime()
        self.db = sqlite3.connect(database_filepath, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cursor = self.db.cursor()
        self.create_tables()
        self.scrape()

    def scrape(self):
        for collection in collection_to_scrape:
            url = base_url + collections_url + collection_to_scrape[collection]
            links = self.get_image_links(url)
            for link in links:
                # insert all the links into the table categorized by collection
                download_link = base_url + link + download_url
                statement = '''INSERT INTO {}(url, lastUsed) VALUES("{}", "0")'''.format(collection, download_link)
                print('Statement is: {}'.format(statement))
                self.db.execute(statement)
            self.db.commit()

    def create_tables(self):
        for collection in collection_to_scrape:
            statement = '''CREATE TABLE if not exists {}(id INTEGER PRIMARY KEY, url TEXT, lastUsed TIMESTAMP)
                '''.format(collection)
            print(statement)
            try:
                self.db.execute(statement)
                self.db.commit()
            except sqlite3.OperationalError:
                # print('Error creating table, they probably already exist')
                pass

    def get_image_links(self, url):
        html = self.get_page_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        anchors = soup.find_all('a', class_='_2Mc8_')
        print('num anchors found: {}'.format(anchors.__len__()))
        anchor_list = []
        for anchor in anchors:
            anchor_list.append(anchor.get('href'))

        return anchor_list

    def get_page_html(self, url):
        # Since this webpage has to load a shitload of images and have lots of javascript
        # we got to be careful with load times and selenium going real fast
        # How it works:
        # - Load website, wait for page to load
        # - scroll to the button
        # - wait again for more stuff to load
        # - scroll again and then click button
        # - scroll to bottom and wait 15 seconds for ALL images to load

        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(url)
        button = driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div[2]/button')

        time.sleep(2)

        driver.execute_script('window.scrollBy(659, 1393)')
        #
        # from selenium.webdriver.common.action_chains import ActionChains
        # ActionChains(driver).move_to_element(button).perform()
        time.sleep(2)
        driver.execute_script('window.scrollBy(659, 1393)')

        button.click()

        driver.execute_script(scroll_to_bottom)
        time.sleep(15)

        return driver.page_source

    def __exit__(self):
        self.db.close()


def database_stats():
    pass


def main():
    scraper = PaperScraper()


if __name__ == '__main__':
    main()



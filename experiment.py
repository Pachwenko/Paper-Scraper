from selenium import webdriver
import time

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

print(driver.page_source)
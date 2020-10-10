import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    link = str(math.ceil(math.pow(math.pi, math.e)*10000))
    button = browser.find_element(By.LINK_TEXT,str(math.ceil(math.pow(math.pi, math.e)*10000)))
    button.click()
    button = browser.find_element(By.NAME, "first_name")
    button.send_keys("testName")
    button = browser.find_element(By.NAME, "last_name")
    button.send_keys("testFam")
    button = browser.find_element(By.NAME, "firstname")
    button.send_keys("testCity")
    button = browser.find_element(By.ID, "country")
    button.send_keys("testCountry")
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
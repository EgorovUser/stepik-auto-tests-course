import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    button = browser.find_element(By.NAME, "first_name")
    button.send_keys("testName")
    button = browser.find_element(By.NAME, "last_name")
    button.send_keys("testFam")
    button = browser.find_element(By.NAME, "firstname")
    button.send_keys("testCity")
    button = browser.find_element(By.ID, "country")
    button.send_keys("testCountry")
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
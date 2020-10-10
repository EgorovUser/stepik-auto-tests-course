import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    button = browser.find_element(By.XPATH, "//div[1]/input")
    button.send_keys("testName")
    button = browser.find_element(By.XPATH, "//div[2]/input")
    button.send_keys("testFam")
    button = browser.find_element(By.XPATH, "//div[3]/input")
    button.send_keys("testCity")
    button = browser.find_element(By.XPATH, "//div[4]/input")
    button.send_keys("testCountry")
    button = browser.find_element(By.XPATH, "//button[contains(text(), \"Submit\")]")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
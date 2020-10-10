import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR,"* input")
    for element in elements:
       element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
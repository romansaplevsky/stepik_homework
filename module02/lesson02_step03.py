from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    x = num1 + num2
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(x))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

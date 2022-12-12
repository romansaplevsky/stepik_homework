from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = calc(browser.find_element(By.ID, "input_value").text)
    form = browser.find_element(By.ID, "answer")
    form.send_keys(x)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

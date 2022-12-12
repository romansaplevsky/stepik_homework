from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = calc(browser.find_element(By.ID, "input_value").text)
    form = browser.find_element(By.ID, "answer")
    form.send_keys(x)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    alert = browser.switch_to.alert
    code = alert.text.split(': ')[-1]
    print(code)
    browser.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
import time


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    price = WebDriverWait(browser, 5).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x = calc(browser.find_element(By.ID, "input_value").text)
    form = browser.find_element(By.ID, "answer")
    form.send_keys(x)
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

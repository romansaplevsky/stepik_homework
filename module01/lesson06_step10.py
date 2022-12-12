from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    first_name_form = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name_form.send_keys("abc")
    last_name_form = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name_form.send_keys("abc")
    email_form = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email_form.send_keys("abc")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_element.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
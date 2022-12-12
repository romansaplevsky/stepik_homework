from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    first_name_form = browser.find_element(By.CSS_SELECTOR, "input[name=\"firstname\"]")
    first_name_form.send_keys("Ivan")
    last_name_form = browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]")
    last_name_form.send_keys("Ivanov")
    email_form = browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]")
    email_form.send_keys("ivanov@ivan.ru")
    file_attach_form = browser.find_element(By.ID, "file")
    current_abspath = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_abspath, "lesson02_step08_textfile.txt")
    file_attach_form.send_keys(file_path)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

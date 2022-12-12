import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(link)
    first_name_form = browser.find_element(By.CSS_SELECTOR, "[name=\"first_name\"]")
    first_name_form.send_keys("Ivan")
    last_name_form = browser.find_element(By.CSS_SELECTOR, "[name=\"last_name\"]")
    last_name_form.send_keys("Petrov")
    city_form = browser.find_element(By.CSS_SELECTOR, ".city")
    city_form.send_keys("Smolensk")
    country_form = browser.find_element(By.ID, "country")
    country_form.send_keys("Russia")
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()

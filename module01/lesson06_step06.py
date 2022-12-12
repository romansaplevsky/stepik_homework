import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    first_name_form = browser.find_element(By.CSS_SELECTOR, "[name=\"first_name\"]")
    first_name_form.send_keys("Ivan")
    last_name_form = browser.find_element(By.CSS_SELECTOR, "[name=\"last_name\"]")
    last_name_form.send_keys("Petrov")
    city_form = browser.find_element(By.CSS_SELECTOR, ".city")
    city_form.send_keys("Smolensk")
    country_form = browser.find_element(By.ID, "country")
    country_form.send_keys("Russia")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()

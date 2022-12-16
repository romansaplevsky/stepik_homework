from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name_form = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name_form.send_keys("abc")
        last_name_form = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name_form.send_keys("abc")
        email_form = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email_form.send_keys("abc")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_element.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        browser.quit()

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name_form = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name_form.send_keys("abc")
        last_name_form = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name_form.send_keys("abc")
        email_form = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email_form.send_keys("abc")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_element = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_element.text
        assert "Congratulations! You have successfully registered!" == welcome_text
        browser.quit()


if __name__ == "__main__":
    unittest.main()


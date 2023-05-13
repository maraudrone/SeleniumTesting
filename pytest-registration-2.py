import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestRegistration:
    @staticmethod
    def register_user(browser, url):
        print("Opening link...")
        browser.get(url)

        print("Entering name...")
        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Vardas")
        print("Entering last name...")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Pavarde")
        print("Entering email...")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("vardaspavarde@email.com")

        print("Pressing the submit button...")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        print("Waiting for 3 seconds...")
        browser.implicitly_wait(3)

        success_text = browser.find_element(By.TAG_NAME, "h1").text
        if "Congratulations! You have successfully registered!" in success_text:
            assert True
            print("Completed!")
        else:
            assert False
            print("Failed!")

    def test_registration1(self, browser):
        self.browser = browser
        self.register_user(browser, "http://suninjuly.github.io/registration1.html")

    def test_registration2(self, browser):
        self.browser = browser
        self.register_user(browser, "http://suninjuly.github.io/registration2.html")

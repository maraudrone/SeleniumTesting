import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):
    browser = webdriver.Chrome()
    request.cls.browser = browser
    yield
    browser.quit()

@pytest.mark.usefixtures("setup")
class TestRegistration:
    def register_user(self, url):
        print("Opening link...")
        self.browser.get(url)

        print("Entering name...")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Vardas")
        print("Entering last name...")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Pavarde")
        print("Entering email...")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("vardaspavarde@email.com")

        print("Pressing the submit button...")
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        print("Waiting for 3 seconds...")
        self.browser.implicitly_wait(3)

        success_text = self.browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" in success_text, "Failed!"
        print("Completed!")

    def test_registration1(self):
        self.register_user("http://suninjuly.github.io/registration1.html")

    def test_registration2(self):
        self.register_user("http://suninjuly.github.io/registration2.html")

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

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
        if "Congratulations! You have successfully registered!" in success_text:
            self.assertTrue(True)
            print("Completed!")
        else:
            self.assertTrue(False)
            print("Failed!")

    def test_registration(self):
        self.register_user("http://suninjuly.github.io/registration1.html")
        self.register_user("http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()

try:
    print("Opening link...")
    browser.get(link)

    print("Clicking button to open a new tab...")
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    print("Switching to the new tab...")
    browser.switch_to.window(browser.window_handles[1])

    print("Finding the value of x...")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    print(f"Value of x is {x}.")

    y = str(math.log(abs(12*math.sin(x))))
    print(f"Entering the value of y ({y})...")
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    print("Submitting form...")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    print("Completed!")

finally:
    print("Closing the browser...")
    browser.quit()

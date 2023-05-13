from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    print("Opening link...")
    browser.get(link)

    print("Pressing button...")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print("Accepting the alert...")
    confirm = browser.switch_to.alert
    confirm.accept()

    print("Finding the value of x...")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Value of x is {x}.")

    y = calc(x)
    print(f"Entering the value of y ({y})...")
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    print("Pressing the submit button...")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print("Printing alert text...")
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    print("Completed!")

finally:
    print("Closing the browser...")
    browser.quit()

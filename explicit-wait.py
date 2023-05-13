from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    print("Opening link...")
    browser.get(link)

    print("Waiting until the price is right...")
    wait = WebDriverWait(browser, 10)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    print("Pressing the book button...")
    bookbutton = browser.find_element(By.ID, "book")
    bookbutton.click()

    print("Solving the equation...")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    print(f"Value of x is {x}.")

    y = str(math.log(abs(12*math.sin(x))))
    print(f"Entering the value of y ({y})...")
    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(y)

    print("Pressing the submit button...")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    print("Completed!")

finally:
    print("Closing the browser...")
    browser.quit()

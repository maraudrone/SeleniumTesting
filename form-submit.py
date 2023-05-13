from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 
link = "http://suninjuly.github.io/simple_form_find_task.html"
 
try:
    browser = webdriver.Chrome()
    print("Opening link...")
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    print("Entering name...")
    input1.send_keys("Vardas")
    input2 = browser.find_element(By.NAME, "last_name")
    print("Entering last name...")
    input2.send_keys("Pavarde")
    input3 = browser.find_element(By.CSS_SELECTOR, ".city")
    print("Entering city...")
    input3.send_keys("Vilnius")
    input4 = browser.find_element(By.ID, "country")
    print("Entering country...")
    input4.send_keys("Lithuania")
    
    button = browser.find_element(By.CSS_SELECTOR, "#submit_button")
    print("Pressing submit button...")
    button.click()
 
finally:
    browser.quit()
    print("Completed!")

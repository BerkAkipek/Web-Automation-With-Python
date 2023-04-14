from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for check_box in check_boxes:
    if check_box.get_attribute("value") == "option2":
        check_box.click()
        assert check_box.is_selected()
        break

radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")

for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio2":
        radio_button.click()
        assert radio_button.is_selected()
        break


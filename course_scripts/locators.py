#!/usr/bin/python3

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("example@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# You can found elements by an xpath syntax:
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# You can find elements with a css selector syntax:
# tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Berk Akipek")

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
sleep(5)

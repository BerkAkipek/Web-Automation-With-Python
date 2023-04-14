#!/usr/bin/python3

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")

# driver.find_element(By.XPATH, "//a[@class='forgot-password-link']").click()

# driver.find_element(By.XPATH, "//input[@placeholder='Enter your email address']").send_keys("demo@gmail.com")

# driver.find_element(By.CSS_SELECTOR, "input[id='userPassword']").send_keys("1346798520")

# driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("1346798520")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(2)

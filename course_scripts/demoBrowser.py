#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractice/#/")
driver.back()
driver.refresh()
driver.forward()
driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[@class='sort-icon sort-descending']").click() # //span[text()='Veg/fruit name']

web_elements = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
actual_list = []
for web_element in web_elements:
    actual_list.append(web_element.text)

sorted_list = sorted(actual_list) # actual_list.sort()

assert actual_list == sorted_list

# if you wanna copy a list use array.copy() method

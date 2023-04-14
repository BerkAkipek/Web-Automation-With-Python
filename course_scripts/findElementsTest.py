from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)


driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
sleep(1)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for country in countries:
    if country.text == 'India':
        country.click()
        break

get_text = driver.find_element(By.ID, "autosuggest").get_attribute("value")

assert "India" in get_text
assert get_text == "India"

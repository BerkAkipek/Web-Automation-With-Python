from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

fname = "Berk"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(fname)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()

alert = driver.switch_to.alert
assert fname in alert.text
alert.accept()

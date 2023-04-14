from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.LINK_TEXT, "Shop").click() # //a[contains(@href,'shop')]

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for elem in products:
    if "Blackberry" in elem.text:
        elem.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.XPATH, "//input[@id='country']").clear()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("india")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

assert "Success" in driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

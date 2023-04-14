from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@class='search-button']").click()

sleep(1)

searched_elements = driver.find_elements(By.XPATH, "//h4")
expected_elements = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
for elem in searched_elements:
    assert elem.text in expected_elements

products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for product in products:
    product.find_element(By.XPATH, "div/button").click() # Every web element carries it's own locator

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
total = 0
for price in prices:
    total += int(price.text)

total_amount = driver.find_element(By.XPATH, "//span[@class='totAmt']")
assert total == int(total_amount.text)

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

assert "Code applied" in driver.find_element(By.CLASS_NAME, "promoInfo").text

discounted_amount = driver.find_element(By.XPATH, "//span[@class='discountAmt']")

assert int(total_amount.text) > float(discounted_amount.text)

# tr td:nth-child(5) p === //tr/td[5]/p


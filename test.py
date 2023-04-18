from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True

driver = webdriver.Chrome("/home/berkakipek/WebDrivers/chromedriver", options=options)

driver.get("https://google.com/")
print(driver.title)
driver.quit()

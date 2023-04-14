from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")


driver.find_element(By.LINK_TEXT, "Click Here").click()

opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])
assert "New Window" in driver.find_element(By.XPATH, "//h3").text

driver.close()

driver.switch_to.window(opened_windows[0])
assert "Opening a new window" in driver.find_element(By.CSS_SELECTOR, "h3").text

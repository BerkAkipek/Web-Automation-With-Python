from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")


driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])

mail = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text

driver.close()

driver.switch_to.window(opened_windows[0])

driver.find_element(By.XPATH, "//input[@id='username']").send_keys(mail)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("p@ssw0rd")
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))

print(driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text)


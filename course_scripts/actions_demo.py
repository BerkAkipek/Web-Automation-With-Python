from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


service_obj = Service("/home/berk/chromedriver/stable/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver=driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


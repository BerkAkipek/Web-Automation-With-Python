import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="class")
def setup(request):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        service_obj = Service("/home/berkakipek/WebDrivers/chromedriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice")
        request.cls.driver = driver
        yield
        driver.close()
        
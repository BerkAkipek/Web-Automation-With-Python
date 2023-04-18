from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
#from ..utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self):

        self.driver.find_element(By.LINK_TEXT, "Shop").click() # //a[contains(@href,'shop')]

        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for elem in products:
            if "Blackberry" in elem.text:
                elem.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        self.driver.find_element(By.XPATH, "//input[@id='country']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("india")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

        assert "Success" in self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text


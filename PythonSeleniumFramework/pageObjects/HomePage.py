from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.shop = (By.LINK_TEXT, "Shop")  # //a[contains(@href,'shop')]
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")

    def shop_items(self):
        self.driver.find_element(*self.shop).click()
        return CheckoutPage(self.driver)

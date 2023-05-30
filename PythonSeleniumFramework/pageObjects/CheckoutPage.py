from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.purchase_button = (By.XPATH, "div/button")
        self.checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def get_product_cards(self):
        return self.driver.find_elements(*self.product_cards)

    def found_purchase_button(self, product):
        return product.find_element(*self.purchase_button)

    def find_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()
        return ConfirmPage(self.driver)

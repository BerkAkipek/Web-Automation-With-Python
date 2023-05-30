from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()

        products = checkout_page.get_product_cards()
        for product in products:
            if "Blackberry" in product.text:
                checkout_page.found_purchase_button(product).click()

        confirm_page = checkout_page.find_checkout_button()
        confirm_page.find_confirm_button().click()

        confirm_page.find_region_input().clear()
        confirm_page.find_region_input().send_keys("india")

        self.verify_link_presence(text="India")

        confirm_page.choose_region().click()
        confirm_page.find_checkbox().click()
        confirm_page.find_purchase_button().click()

        assert "Success" in confirm_page.find_success_message().text

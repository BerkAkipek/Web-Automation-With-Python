from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
        self.confirm_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.region_input = (By.XPATH, "//input[@id='country']")
        self.region_text = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//label[@for='checkbox2']")
        self.purchase_button = (By.XPATH, "//input[@value='Purchase']")
        self.success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def find_confirm_button(self):
        return self.driver.find_element(*self.confirm_button)

    def find_region_input(self):
        return self.driver.find_element(*self.region_input)

    def choose_region(self):
        return self.driver.find_element(*self.region_text)

    def find_checkbox(self):
        return self.driver.find_element(*self.checkbox)

    def find_purchase_button(self):
        return self.driver.find_element(*self.purchase_button)

    def find_success_message(self):
        return self.driver.find_element(*self.success_message)

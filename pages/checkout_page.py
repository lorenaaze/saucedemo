from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.button_checkout_at_cart = (By.ID, "checkout")
        self.name_field = (By.ID, "first-name")
        self.lastname_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.button_continue = (By.ID, "continue")
        self.button_finish = (By.ID, "finish")
        self.thanks_for_order_text = (By.XPATH, "//h2[contains(text(), 'Thank you for your order!')]")

    def click_checkout_at_cart(self):
        self.click_locator(self.button_checkout_at_cart)

    def fill_out_the_fields(self, name, lastname, postal_code):
        self.send_text(self.name_field, name)
        self.send_text(self.lastname_field, lastname)
        self.send_text(self.postal_code_field, postal_code)

    def create_order(self):
        self.click_locator(self.button_continue)
        self.click_locator(self.button_finish)

    def check_finished_order(self):
        self.check_if_element_exists(self.thanks_for_order_text)


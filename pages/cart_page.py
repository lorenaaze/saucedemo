from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item = (By.XPATH, "//div[contains(text(), '{}')]")
        self.button_continue_shopping = (By.ID, "continue-shopping")

    def check_item_at_cart(self, item_name):
        item = (self.item[0], self.item[1].format(item_name))
        self.check_if_element_exists(item)

    def click_continue_shopping(self):
        self.click_locator(self.button_continue_shopping)
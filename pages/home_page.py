from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
        self.item = (By.XPATH, "//div[contains(text(), '{}')]")
        self.button_add_cart = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def check_login(self):
        self.check_if_element_exists(self.page_title)

    def add_to_cart_item(self, item_name):
        item = (self.item[0], self.item[1].format(item_name))
        self.click_locator(item)
        self.click_locator(self.button_add_cart)

    def check_cart(self):
        self.click_locator(self.cart_icon)

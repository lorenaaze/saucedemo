from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def to_sign_in(self, user, password):
        self.send_text(self.username_field, user)
        self.send_text(self.password_field, password)
        self.click_locator(self.login_button)
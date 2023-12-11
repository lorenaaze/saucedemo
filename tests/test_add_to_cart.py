import time
import pytest
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")

class TestCT02:
    @staticmethod
    def test_ct02_add_to_cart():

        login_page = LoginPage()
        home_page = HomePage()
        cart_page = CartPage()
        item_1 = "Sauce Labs Bike Light"
        item_2 = "Sauce Labs Onesie"

        #faz o login
        login_page.to_sign_in("standard_user", "secret_sauce")

        #adiciona primeiro item e checa no carrinho
        home_page.add_to_cart_item(item_1)
        home_page.check_cart()
        cart_page.check_item_at_cart(item_1)
        time.sleep(2)

        #adiciona segundo item e checa no carrinho
        cart_page.click_continue_shopping()
        home_page.add_to_cart_item(item_2)
        home_page.check_cart()
        cart_page.check_item_at_cart(item_2)
        time.sleep(2)

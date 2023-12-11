import time
import pytest
from pages.checkout_page import CheckoutPage
from tests.test_add_to_cart import TestCT02

@pytest.mark.usefixtures("setup_teardown")

class TestCT03:
    def test_ct03_finish_order(self):
        checkout_page = CheckoutPage()

        #chama método de adicionar no carrinho
        TestCT02().test_ct02_add_to_cart()

        #faz checkout e finaliza compra
        checkout_page.click_checkout_at_cart()
        checkout_page.fill_out_the_fields("teste nome", "teste sobrenome", "123456789")
        time.sleep(5)
        checkout_page.create_order()
        checkout_page.check_finished_order()
        time.sleep(3)


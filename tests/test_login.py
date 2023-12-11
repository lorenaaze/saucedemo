import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login(self):

        login_page = LoginPage()
        home_page = HomePage()

        login_page.to_sign_in("standard_user", "secret_sauce")
        home_page.check_login()
        time.sleep(3)

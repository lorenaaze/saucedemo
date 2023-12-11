import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def search_element(self, locator):
        return self.driver.find_element(*locator)

    def send_text(self, locator, text):
        self.search_element(locator).send_keys(text)

    def click_locator(self, locator):
        self.search_element(locator).click()

    def check_if_element_exists(self, locator):
        assert self.search_element(locator).is_displayed(), "Elemento não encontrado"


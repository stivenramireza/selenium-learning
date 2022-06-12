from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from tests.test_ecommerce import EcommerceTest


class AssertionsTest(EcommerceTest):
    def is_element_present(self, how: str, what: str) -> None:
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        else:
            return True

    def test_search_field(self) -> None:
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self) -> None:
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

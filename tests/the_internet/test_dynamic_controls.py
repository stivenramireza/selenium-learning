from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.the_internet.test_the_internet import TheInternetTestCase


class DynamicControlsTestCase(TheInternetTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self) -> None:
        checkbox = self.driver.find_element_by_css_selector(
            '#checkbox > input[type=checkbox]'
        )
        checkbox.click()

        remove_add_button = self.driver.find_element_by_css_selector(
            '#checkbox-example > button'
        )
        remove_add_button.click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#checkbox-example > button')
            )
        )
        remove_add_button.click()

        enable_disable_button = self.driver.find_element_by_css_selector(
            '#input-example > button'
        )
        enable_disable_button.click()

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#input-example > button')
            )
        )

        text_area = self.driver.find_element_by_css_selector(
            '#input-example > input[type=text]'
        )
        text_area.send_keys('stivenramireza')

        enable_disable_button.click()

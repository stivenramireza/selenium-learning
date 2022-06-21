from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:
    def __init__(self, driver: Chrome) -> None:
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'

    @property
    def is_loaded(self) -> bool:
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.search_locator))
        )
        return True

    @property
    def keyword(self) -> str:
        input_field = self._driver.find_element_by_name(self.search_locator)
        return input_field.get_attribute('value')

    def open(self) -> None:
        self._driver.get(self._url)

    def type_search(self, keyword: str) -> None:
        input_field = self._driver.find_element_by_name(self.search_locator)
        input_field.send_keys(keyword)

    def click_submit(self) -> None:
        input_field = self._driver.find_element_by_name(self.search_locator)
        input_field.submit()

    def search(self, keyword: str) -> None:
        self.type_search(keyword)
        self.click_submit()

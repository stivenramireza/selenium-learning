import unittest

from selenium import webdriver

from src.secrets import DRIVER_PATH


class MercadoLibreTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://www.mercadolibre.com')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_search_ps4(self) -> None:
        country = self.driver.find_element_by_id('CO')
        country.click()

        search_field = self.driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()

        filter_element = self.driver.find_element_by_class_name(
            'ui-search-filter-name'
        )
        if filter_element.text == 'Bogotá D.C.':
            filter_element.click()

        if filter_element.text == 'Nuevo':
            filter_element.click()

        order_button = self.driver.find_element_by_class_name(
            'andes-dropdown__trigger'
        )
        order_button.click()

        higher_price = self.driver.find_element_by_id(
            'andes-dropdown-más-relevantes-list-option-price_desc'
        )
        higher_price.click()

        articles = [
            self.driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2'
            ).text
            for i in range(5)
        ]
        prices = [
            self.driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]'
            ).text
            for i in range(5)
        ]

        print(articles)
        print(prices)

from tests.test_ecommerce import EcommerceTestCase


class SearchTestCase(EcommerceTestCase):
    def test_search_tee(self) -> None:
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        products_counter = self.driver.find_element_by_css_selector(
            'div.count-container p.amount'
        )
        self.assertAlmostEqual(products_counter.text, '5 Item(s)')

    def test_search_salt_shaker(self) -> None:
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a'
        )
        self.assertEqual(len(products), 1)

from ddt import ddt, data, unpack

from tests.ecommerce.test_ecommerce import EcommerceTestCase


@ddt
class SearchDDTTestCase(EcommerceTestCase):
    @data(('dress', 5), ('music', 5))
    @unpack
    def test_search_ddt(self, search_value: str, expected_count: int) -> None:
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//h2[@class="product-name"]/a'
        )
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

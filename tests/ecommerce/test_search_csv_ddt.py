import csv

from ddt import ddt, data, unpack

from tests.ecommerce.test_ecommerce import EcommerceTestCase


def get_data(file_name: str) -> None:
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    return [row for row in reader]


@ddt
class SearchCSVDDTTestCase(EcommerceTestCase):
    @data(*get_data('tests/ecommerce/files/test_data.csv'))
    @unpack
    def test_search_ddt(self, search_value: str, expected_count: int) -> None:
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = self.driver.find_elements_by_xpath(
            '//h2[@class="product-name"]/a'
        )
        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = self.driver.find_element_by_class_name('not-msg')
            self.assertEqual(message, 'Your search returns no results.')

        print(f'Found {len(products)} products')

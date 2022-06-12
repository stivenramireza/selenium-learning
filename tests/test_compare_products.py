from tests.test_ecommerce import EcommerceTestCase


class CompareProductsTestCase(EcommerceTestCase):
    def test_compare_products_removal_alert(self) -> None:
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        self.driver.find_element_by_class_name('link-compare').click()
        self.driver.find_element_by_link_text('Clear All').click()

        alert = self.driver.switch_to.alert
        alert_text = alert.text

        self.assertEqual(
            alert_text,
            'Are you sure you would like to remove all products from your comparison?',
        )

        alert.accept()

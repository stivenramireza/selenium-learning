from tests.ecommerce.test_ecommerce import EcommerceTestCase


class NavigationTestCase(EcommerceTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.get('https://www.google.com')

    def test_browser_navigation(self) -> None:
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

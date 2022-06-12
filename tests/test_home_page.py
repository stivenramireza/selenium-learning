from tests.test_ecommerce import EcommerceTestCase


class HomePageTestCase(EcommerceTestCase):
    def test_search_text_field(self) -> None:
        self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self) -> None:
        self.driver.find_element_by_name('q')

    def test_search_text_field_by_class_name(self) -> None:
        self.driver.find_element_by_class_name('input-text')

    def test_search_button_enabled(self) -> None:
        self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self) -> None:
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(len(banners), 3)

    def test_vip_promo(self) -> None:
        self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img'
        )

    def test_shopping_cart(self) -> None:
        self.driver.find_element_by_css_selector(
            'div.header-minicart span.icon'
        )

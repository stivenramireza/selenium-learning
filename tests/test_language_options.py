from selenium.webdriver.support.ui import Select

from tests.test_ecommerce import EcommerceTestCase


class LanguageOptionsTestCase(EcommerceTestCase):
    def test_select_language(self) -> None:
        exp_options = ['English', 'French', 'German']
        act_options = []

        select_language = Select(
            self.driver.find_element_by_id('select-language')
        )

        self.assertEqual(len(select_language.options), 3)

        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(act_options, exp_options)

        self.assertEqual(select_language.first_selected_option.text, 'English')

        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(
            self.driver.find_element_by_id('select-language')
        )
        select_language.select_by_index(0)

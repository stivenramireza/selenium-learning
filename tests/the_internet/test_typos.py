from tests.the_internet.test_the_internet import TheInternetTestCase


class TyposTestCase(TheInternetTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self) -> None:
        paragraph_to_check = self.driver.find_element_by_css_selector(
            '#content > div > p:nth-child(3)'
        )
        text_to_check = paragraph_to_check.text

        tries = 1
        found = False

        correct_text = 'Sometimes you\'ll see a typo, other times you won\'t.'

        while text_to_check != correct_text:
            paragraph_to_check = self.driver.find_element_by_css_selector(
                '#content > div > p:nth-child(3)'
            )
            text_to_check = paragraph_to_check.text
            self.driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                self.driver.refresh()
                found = True

        self.assertTrue(found)

        print(f'It took {tries} tries to find the typo')

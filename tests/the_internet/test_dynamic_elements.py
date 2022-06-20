from tests.the_internet.test_the_internet import TheInternetTestCase


class DynamicElementsTestCase(TheInternetTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self) -> None:
        options = []
        menu = 4
        tries = 1

        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    option_name = self.driver.find_element_by_xpath(
                        f'//*[@id="content"]/div/ul/li[{i + 1}]/a'
                    )
                    options.append(option_name.text)
                    print(options)
                except Exception:
                    print(f'Option number {i + 1} is not found')
                    tries += 1
                    self.driver.refresh()

        print(f'Finished in {tries} tries')

from time import sleep

from tests.the_internet.test_the_internet import TheInternetTestCase


class AddRemoveElementsTestCase(TheInternetTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self) -> None:
        added_elements = 5
        removed_elements = 6
        total_elements = added_elements - removed_elements

        add_button = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/button'
        )
        sleep(3)

        for i in range(added_elements):
            add_button.click()

        for i in range(removed_elements):
            try:
                delete_button = self.driver.find_element_by_class_name(
                    'added-manually'
                )
                delete_button.click()
            except Exception:
                print(
                    'You\'re trying to delete more elements than the existent'
                )
                break

        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print('There are 0 elements on screen')

        sleep(3)

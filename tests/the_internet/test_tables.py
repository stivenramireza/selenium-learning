from tests.the_internet.test_the_internet import TheInternetTestCase


class TablesTestCase(TheInternetTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self) -> None:
        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = self.driver.find_element_by_xpath(
                f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span'
            )
            table_data[i].append(header.text)

            for j in range(4):
                row_data = self.driver.find_element_by_xpath(
                    f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]'
                )
                table_data[i].append(row_data.text)

        print(table_data)

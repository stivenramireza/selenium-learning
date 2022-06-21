from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from tests.ecommerce.test_assertions import AssertionsTestCase
from tests.ecommerce.test_search import SearchTestCase
from tests.ecommerce.test_search_ddt import SearchDDTTestCase
from tests.ecommerce.test_search_csv_ddt import SearchCSVDDTTestCase

from tests.the_internet.test_add_remove_elements import (
    AddRemoveElementsTestCase,
)
from tests.the_internet.test_dynamic_elements import DynamicElementsTestCase
from tests.the_internet.test_dynamic_controls import DynamicControlsTestCase
from tests.the_internet.test_typos import TyposTestCase
from tests.the_internet.test_tables import TablesTestCase


def run_ecommerce_tests() -> None:
    assertions_test_case = TestLoader().loadTestsFromTestCase(
        AssertionsTestCase
    )
    search_test_case = TestLoader().loadTestsFromTestCase(SearchTestCase)
    search_ddt_test_case = TestLoader().loadTestsFromTestCase(SearchDDTTestCase)
    search_csv_ddt_test_case = TestLoader().loadTestsFromTestCase(
        SearchCSVDDTTestCase
    )

    smoke_test = TestSuite([search_csv_ddt_test_case])

    kwargs = {'output': 'ecommerce-report'}

    runner = HTMLTestRunner(**kwargs)
    runner.run(smoke_test)


def run_the_internet_tests() -> None:
    add_remove_elements_test_case = TestLoader().loadTestsFromTestCase(
        AddRemoveElementsTestCase
    )
    dynamic_elements_test_case = TestLoader().loadTestsFromTestCase(
        DynamicElementsTestCase
    )
    dynamic_controls_test_case = TestLoader().loadTestsFromTestCase(
        DynamicControlsTestCase
    )
    typos_test_case = TestLoader().loadTestsFromTestCase(TyposTestCase)
    tables_test_case = TestLoader().loadTestsFromTestCase(TablesTestCase)

    smoke_test = TestSuite(
        [
            add_remove_elements_test_case,
            dynamic_elements_test_case,
            dynamic_controls_test_case,
            typos_test_case,
            tables_test_case,
        ]
    )

    kwargs = {'output': 'the-internet-report'}

    runner = HTMLTestRunner(**kwargs)
    runner.run(smoke_test)


def main() -> None:
    ##Ecommerce tests
    run_ecommerce_tests()

    # The Internet tests
    # run_the_internet_tests()


if __name__ == '__main__':
    main()

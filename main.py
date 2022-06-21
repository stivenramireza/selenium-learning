from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from tests.ecommerce.test_assertions import AssertionsTestCase
from tests.ecommerce.test_search import SearchTestCase

from tests.the_internet.test_add_remove_elements import (
    AddRemoveElementsTestCase,
)
from tests.the_internet.test_dynamic_elements import DynamicElementsTestCase
from tests.the_internet.test_dynamic_controls import DynamicControlsTestCase
from tests.the_internet.test_typos import TyposTestCase


def run_ecommerce_tests() -> None:
    assertions_test_case = TestLoader().loadTestsFromTestCase(
        AssertionsTestCase
    )
    search_test_case = TestLoader().loadTestsFromTestCase(SearchTestCase)

    smoke_test = TestSuite([assertions_test_case, search_test_case])

    kwargs = {'output': 'smoke-report'}

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

    smoke_test = TestSuite(
        [
            # add_remove_elements_test_case,
            # dynamic_elements_test_case,
            # dynamic_controls_test_case,
            typos_test_case
        ]
    )

    kwargs = {'output': 'the-internet-report'}

    runner = HTMLTestRunner(**kwargs)
    runner.run(smoke_test)


def main() -> None:
    ##Ecommerce tests
    # run_ecommerce_tests()

    # The Internet tests
    run_the_internet_tests()


if __name__ == '__main__':
    main()

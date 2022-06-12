from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner

from tests.test_assertions import AssertionsTestCase
from tests.test_search import SearchTestCase


def main() -> None:
    assertions_test_case = TestLoader().loadTestsFromTestCase(
        AssertionsTestCase
    )
    search_test_case = TestLoader().loadTestsFromTestCase(SearchTestCase)

    smoke_test = TestSuite([assertions_test_case, search_test_case])

    kwargs = {'output': 'smoke-report'}

    runner = HTMLTestRunner(**kwargs)
    runner.run(smoke_test)


if __name__ == '__main__':
    main()

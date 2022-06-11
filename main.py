import unittest
from pyunitreport import HTMLTestRunner


def main() -> None:
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports', report_name='hello-world-report'
        ),
    )


if __name__ == '__main__':
    main()

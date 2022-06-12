import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

from src.secrets import DRIVER_PATH


class EcommerceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.implicitly_wait(10)
        self.driver.get('http://demo-store.seleniumacademy.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(
            output='reports', report_name='ecommerce-report'
        ),
    )

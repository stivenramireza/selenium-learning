import unittest

from selenium import webdriver

from src.secrets import DRIVER_PATH


class TheInternetTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://the-internet.herokuapp.com/')

    def tearDown(self) -> None:
        self.driver.close()

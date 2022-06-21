import unittest

from selenium import webdriver

from tests.pom.google_page import GooglePage
from src.secrets import DRIVER_PATH


class GoogleTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    def test_search(self) -> None:
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual(google.keyword, 'Platzi')

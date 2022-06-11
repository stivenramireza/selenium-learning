import unittest
from selenium import webdriver

from src.secrets import DRIVER_PATH


class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        cls.driver.implicitly_wait(10)

    def test_hello_world(self) -> None:
        self.driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self) -> None:
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

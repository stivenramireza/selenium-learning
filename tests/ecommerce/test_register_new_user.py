from tests.ecommerce.test_ecommerce import EcommerceTestCase


class RegisterNewUserTestCase(EcommerceTestCase):
    def test_new_user(self) -> None:
        self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]'
        ).click()
        self.driver.find_element_by_link_text('Log In').click()

        create_account_button = self.driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span'
        )
        self.assertTrue(
            create_account_button.is_displayed()
            and create_account_button.is_enabled()
        )
        create_account_button.click()

        self.assertEqual(self.driver.title, 'Create New Customer Account')

        first_name = self.driver.find_element_by_id('firstname')
        middle_name = self.driver.find_element_by_id('middlename')
        last_name = self.driver.find_element_by_id('lastname')
        email_address = self.driver.find_element_by_id('email_address')
        news_letter_subcription = self.driver.find_element_by_id(
            'is_subscribed'
        )
        password = self.driver.find_element_by_id('password')
        confirm_password = self.driver.find_element_by_id('confirmation')
        submit_button = self.driver.find_element_by_xpath(
            '//*[@id="form-validate"]/div[2]/button/span/span'
        )

        self.assertTrue(
            first_name.is_enabled()
            and middle_name.is_enabled()
            and last_name.is_enabled()
            and email_address.is_enabled()
            and email_address.is_enabled()
            and news_letter_subcription.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and submit_button.is_enabled()
        )

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('test@gmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

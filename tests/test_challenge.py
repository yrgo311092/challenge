import time
import unittest
from config.Test_data import BaseTest
from pages.pages_elements import Elements



class Challenge_Baufest(BaseTest):

    def test_a_onboarding(self):
        onboarding_user = Elements(self.driver)
        onboarding_user.click_singup_button()
        onboarding_user.input_username_onboarding()
        onboarding_user.input_password_onboarding()
        onboarding_user.click_finish_onboarding()
        time.sleep(1)
        self.driver.switch_to.alert.accept()

    def test_b_login_and_logout(self):
        login = Elements(self.driver)
        login.click_button_login()
        login.input_username_login()
        login.input_password_login()
        login.click_button_finish_login()
        validation_login = login.show_name_of_user()
        self.assertTrue(validation_login.is_displayed())
        login.click_button_logout()
        validation_logout = login.click_button_login()
        self.assertTrue(validation_logout.is_displayed())

    def test_checkout(self):
        checkout = Elements(self.driver)
        checkout.login_succesfull()
        time.sleep(1)
        checkout.click_button_laptops()
        checkout.click_product()
        checkout.click_button_add_cart()
        checkout.click_button_cart()
        assert checkout.input_price_cart() != 0


if __name__ == '__main__':
    unittest.main()

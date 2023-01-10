from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Remote
from pages.base_page import BasePage
from config.data_common import info_common
from selenium.webdriver import Keys


class Elements(BasePage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.driver = driver

    def click_singup_button(self):
        button_category = self.wait_element_is_clickable(By.ID, "signin2")
        ActionChains(self.driver).move_to_element(button_category).click().perform()

    def input_username_onboarding(self):
        input_static = self.wait_element_visible(By.ID, "sign-username")
        input_static.send_keys(info_common.username)

    def input_password_onboarding(self):
        password = self.wait_element_visible(By.ID, "sign-password")
        password.send_keys(info_common.password)

    def click_finish_onboarding(self):
        self.wait_element_is_clickable(By.CSS_SELECTOR, "button[onclick='register()']").click()

    def click_button_login(self):
        button_finish = self.driver.find_element(By.ID, "login2")
        button_finish.click()
        return button_finish

    def click_close_modal(self):
        self.driver.find_element(By.CLASS_NAME, "close").click()

    def click_button_finish_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()

    def input_username_login(self):
        user_login = self.driver.find_element(By.ID, "loginusername")
        user_login.send_keys(info_common.username)

    def input_password_login(self):
        pass_login = self.driver.find_element(By.ID, "loginpassword")
        pass_login.send_keys(info_common.password)

    def show_name_of_user(self):
        show_user = self.wait_element_visible(By.ID, "nameofuser")
        return show_user

    def click_button_logout(self):
        self.wait_element_visible(By.ID, "logout2").click()

    def login_succesfull(self):
        login_method = Elements(self.driver)
        login_method.click_button_login()
        login_method.input_username_login()
        login_method.input_password_login()
        login_method.click_button_finish_login()
        return login_method

    def click_button_laptops(self):
        self.wait_element_by_located(By.XPATH, "(//a[normalize-space()='Laptops'])[1]").click()

    def click_product(self):
        self.driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()

    def click_button_add_cart(self):
        add_cart = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Add to cart'])[1]")
        add_cart.click()
        add_cart.send_keys(Keys.ENTER)

    def click_button_cart(self):
        self.driver.find_element(By.XPATH, "(//a[normalize-space()='Cart'])[1]").click()

    def input_price_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#totalp")



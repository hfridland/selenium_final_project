from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)


    def register_new_user(self, email, password):
        email_element = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_element.send_keys(email)
        password_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_element.send_keys(password)
        password1_element = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1_element.send_keys(password)
        reg_btn_element = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_btn_element.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "No substring 'login' in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

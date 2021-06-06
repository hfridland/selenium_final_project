from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_link.click()
        self.solve_quiz_and_get_code()
        self.test_message(product_name, product_price)

    def click_add_to_basket_button(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_link.click()

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_element.text

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_element.text

    def test_message(self, product_name, product_price):
        msg = self.browser.find_elements(*ProductPageLocators.MSG_PRODUCT)
        assert len(msg) == 3, f"Number of messages error. Expected: 3, actual: {len(msg)}"
        assert product_name == msg[0].text, f"Wrong product name. Expected: {product_name}, actual: {msg[0].text}"
        assert product_price == msg[2].text, f"Wrong product price. Expected: {product_price}, actual: {msg[2].text}"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

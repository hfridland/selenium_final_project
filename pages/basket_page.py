from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def is_basket_empty(self):
        try :
            WebDriverWait(self.browser, 4).until_not(EC.presence_of_all_elements_located(BasketPageLocators.BASKET_ITEMS))
        except TimeoutException:
            return False
        return True

    def is_emptymsg_present(self):
        try:
            element = self.browser.find_element(*BasketPageLocators.MSG_BASKET_EMPTY)
            return element.text.strip().startswith("Your basket is empty.")
        except NoSuchElementException:
            return False

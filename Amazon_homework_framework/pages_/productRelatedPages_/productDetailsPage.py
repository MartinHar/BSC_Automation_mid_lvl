from selenium.webdriver.common.by import By
from Amazon_homework_framework.pages_.basePage_ import BasePage


class ProductDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__addToCart = (By.ID, "add-to-cart-button")

    def click_add_to_cart_btn(self):
        add_to_cart = self._find_element(self.__addToCart)
        add_to_cart.click()

from selenium.webdriver.common.by import By
from Amazon_homework_framework.pages_.basePage_ import BasePage


class SearchResult(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # self.__firstResult = (By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[3]")
        # self.__firstResult = (By.XPATH, "(//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'])[1]")
        self.__firstResult = (By.XPATH, "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[1]")

    def click_to_first_result(self):
        first_result = self._find_element(self.__firstResult)
        first_result.click()
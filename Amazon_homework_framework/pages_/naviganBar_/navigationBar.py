from selenium.webdriver.common.by import By
from Amazon_homework_framework.pages_.basePage_ import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__userNameLocator = (By.ID, "nav-link-accountList-nav-line-1")
        self.__searchBox = (By.ID, "twotabsearchtextbox")
        self.__searchBtn = (By.ID, "nav-search-submit-button")

    def get_user_name(self):
        # userNameElement = self.driver.find_element(*self.__userNameLocator)
        userNameElement = self._find_element(self.__userNameLocator)
        return (userNameElement.text.split(" "))[1]

    def fill_text_in_search_box(self, text):
        searchBox = self._find_element(self.__searchBox)
        searchBox.clear()
        searchBox.send_keys(text)

    def click_search_btn(self):
        searchBtn = self._find_element(self.__searchBtn)
        searchBtn.click()

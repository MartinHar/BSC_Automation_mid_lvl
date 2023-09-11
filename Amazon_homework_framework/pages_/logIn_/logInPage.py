from selenium import webdriver
from selenium.webdriver.common.by import By

from Amazon_homework_framework.pages_.basePage_ import BasePage


class LogIn(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

        self.__loginFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")

    def fill_login_field(self, login):
        loginFieldElement = self._find_element(self.__loginFieldLocator)
        loginFieldElement.clear()
        loginFieldElement.send_keys(login)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, passwd):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(passwd)


    def click_to_sign_in_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        signInButtonElement.click()
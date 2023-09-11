import time
import unittest
from selenium import webdriver

from Amazon_homework_framework.pages_.logIn_.logInPage import LogIn
from Amazon_homework_framework.pages_.naviganBar_.navigationBar import NavigationBar


class LogInTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_valid_login(self):
        loginPageObj = LogIn(self.driver)

        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun321")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()

        #Assertion
        navigationBarObj = NavigationBar(self.driver)
        self.assertEqual(navigationBarObj.get_user_name(), "Fname")

    def tearDown(self) -> None:
        time.sleep(17)
        self.driver.close()


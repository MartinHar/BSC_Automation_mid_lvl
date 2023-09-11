import time
import unittest
from selenium import webdriver

from Amazon_homework_framework.pages_.logIn_.logInPage import LogIn
from Amazon_homework_framework.pages_.naviganBar_.navigationBar import NavigationBar
from Amazon_homework_framework.pages_.productRelatedPages_.productDetailsPage import ProductDetails
from Amazon_homework_framework.pages_.productRelatedPages_.searchResultPage import SearchResult

# todo 1) login > search text > from result click to 1st product > add to cart          √
# todo 2) open cart > delete 1st product, 2nd method open cart > delete all products
# todo 3) check login functionality -- invalid password and validate error message


class AddToCartFirstProduct(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_login(self):
        loginPageObj = LogIn(self.driver)
        navBarObj = NavigationBar(self.driver)
        searchResultObj = SearchResult(self.driver)
        productDetailsObj = ProductDetails(self.driver)

        loginPageObj.fill_login_field("test_armenia_99@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("anunazganun321")
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()
        navBarObj.fill_text_in_search_box("razer")
        navBarObj.click_search_btn()
        searchResultObj.click_to_first_result()
        productDetailsObj.click_add_to_cart_btn()

    def tearDown(self) -> None:
        time.sleep(17)
        self.driver.close()


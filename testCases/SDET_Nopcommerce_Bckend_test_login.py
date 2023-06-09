import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURl)
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

        def test_login(self,setup):
            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp=Login_Page(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title=self.driver.title
            self.driver.close()
            if act_title =="Dashboard / nopCommerce administration":
                assert True
            else:
                assert False


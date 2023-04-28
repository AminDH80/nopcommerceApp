import pytest
import time
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("********SearchCustomerByEmail_004*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login succesful****")
        self.logger.info("******Starting Search Customer By Email*****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********* searching customer by emailID*****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        statuts=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == statuts
        self.logger.info("******* TC_SearchCustomerByEmail_004 Finished*****")


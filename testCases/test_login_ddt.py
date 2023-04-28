import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger =LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
            self.logger.info("*************Test_002_DDT_Login*************")
            self.logger.info("*************Verifying Login Test***********")
            self.driver = setup
            self.driver.get(self.baseUrl)
            self.lp=LoginPage(self.driver)

            self.rows =XLUtils.getRowCount(self.path,'Feuil1')
            print("Number of Rows i a Excel",self.rows)

            lst_statuts =[]  #Empty list variable

            for r in range (2,self.rows+1):
                self.user=XLUtils.readData(self.path,'Feuil1',r, 1)
                self.password = XLUtils.readData(self.path, 'Feuil1',r, 2)
                self.exp = XLUtils.readData(self.path,'Feuil1', r, 3)

                self.lp.setUserName(self.user)
                self.lp.setPassword(self.password )
                self.lp.clickLogin()
                time.sleep(5)

                act_title =self.driver.title
                exp_title ="Dashboard / nopCommerce administration"

                if act_title==exp_title:
                    if self.exp=="Pass":
                        self.logger.info("***Passed***")
                        self.lp.clickLogout();
                        lst_statuts.append("Pass")
                    elif self.exp=="Fail":
                        self.logger.info("***failed***")
                        self.lp.clickLogout();
                        lst_statuts.append("Fail")

                elif act_title != exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("**** failed ****")
                        lst_statuts.append("Fail")
                    elif self.exp =='Fail':
                        self.logger.info("**** passed ****")
                        lst_statuts.append("Pass")

            if "Fail" not in lst_statuts :
                self.logger.info("**** Login DDT test Passed ****")
                self.driver.close()
                assert True
            else:
                self.logger.info("**** Login DDT test failed ****")
                self.driver.close()
                assert False

            self.logger.info("******* End of Login DDT Test*******")
            self.logger.info("***************** Completed TC_LoginDDT_002 **************");







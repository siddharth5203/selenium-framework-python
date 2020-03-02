import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,DataProvider,AbstractSelenium,LoginPage

class LoginTest(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize("userName", [("srb")])
    def test_verifyLoginForExpiredUser(self,userName):
        print("First Testcase",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForExpiredPassword(userName).printErrorMessage()

    @pytest.mark.parametrize("userName", [("srbhavsar"),("srb")])
    def test_verifyLoginForInvalidUser(self,userName):
        print("Second Testcase",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)

    @pytest.mark.parametrize("TC_ID,TC_NAME,userName",DataProvider.DataProvider.getData("test_verifyLoginForInvalidUser"))
    def test_verifyLoginForInvalidUser(self,TC_ID,TC_NAME,userName):
        print("Third Testcase",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)
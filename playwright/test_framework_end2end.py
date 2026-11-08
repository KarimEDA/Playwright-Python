import json, pytest
from playwright.sync_api import Playwright
from utils.apiBaseFramework import APIUtils
from pageObjects.logIn import logInPage

# Data
with open('C:/Users/PC/PycharmProjects/PythonProject/PytestPython/playwright/data/moreCredentials.json', 'r') as f:
    testData = json.load(f)
    validUsers = testData['userCredentials'][0]['validUser']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', validUsers, indirect=True)
def test_end2endWebAPI(pageInit, playwright: Playwright, user_credentials):

    # Data init
    username = user_credentials['username']
    pwd = user_credentials['password']
    # Create order
    api = APIUtils()
    orderID = api.createOrder(playwright, username, pwd)
    # Log in - Browser initialization
    logInObj = logInPage(pageInit, pwd)
    logInObj.goToLoginPage()
    dashboardObj = logInObj.logIn(username)
    #Order history
    orderObj = dashboardObj.goToOrders()
    detailsObj = orderObj.selectOrder(orderID)
    # Validate order
    detailsObj.validation()

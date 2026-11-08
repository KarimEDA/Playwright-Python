from xml import parsers

from pytest_bdd import given, when, then, parsers, scenarios
import pytest
from pageObjects.logIn import logInPage
from utils.apiBaseFramework import APIUtils

scenarios('features/orderTransaction.feature')

@given(parsers.parse('create order with {username} and {password}'))
def place_item_order(username, password, shared_data, playwright):
    api = APIUtils()
    orderID = api.createOrder(playwright, username, password)
    shared_data['username'] = username
    shared_data['password'] = password
    shared_data['orderID'] = orderID

@given('user is on landing page')
def user_is_on_landing_page(pageInit, shared_data):
    password = shared_data['password']
    logInObj = logInPage(pageInit, password)
    logInObj.goToLoginPage()
    shared_data['logInObj'] = logInObj

@when(parsers.parse('I login to portal with {username} and {password}'))
def log_in_portal(username, password, shared_data):
    logInObj = shared_data['logInObj']
    dashboardObj = logInObj.logIn(username)
    shared_data['dashboardObj'] = dashboardObj

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardObj = shared_data['dashboardObj']
    orderObj = dashboardObj.goToOrders()
    shared_data['orderObj'] = orderObj

@when('select the orderID')
def select_orderID(shared_data):
    orderObj = shared_data['orderObj']
    orderID = shared_data['orderID']
    detailsObj = orderObj.selectOrder(orderID)
    shared_data['detailsObj'] = detailsObj

@then('order message is successfully displayed')
def order_message(shared_data):
    detailsObj = shared_data['detailsObj']
    detailsObj.validation()
    print(shared_data)

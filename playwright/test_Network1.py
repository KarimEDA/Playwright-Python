import time, pytest
from utils.apiBase import APIUtils
from playwright.sync_api import Page, expect, Playwright

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def interceptResponse(route):
    route.fulfill(
        json= fakePayloadOrderResponse
    )

def interceptRequest(route):
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=xxxxxxxxx')

@pytest.mark.smoke
def test_network1(page: Page):

    #Listener: Routing provides the capability to modify network requests that are made by a page.
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", interceptResponse)

    # Log in
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("eduardwayne1987@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Eduardwayne1987*")
    page.get_by_role("button").click()

    # Go to orders page
    page.get_by_role("button", name='ORDERS').click()

    # Validations
    expect(page.locator('.mt-4.ng-star-inserted')).to_contain_text('You have No Orders to show at this time.')
    time.sleep(5)

@pytest.mark.smoke
def test_network2(page: Page):

    #Listener: Routing provides the capability to modify network requests that are made by a page.
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)

    # Log in
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("eduardwayne1987@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Eduardwayne1987*")
    page.get_by_role("button").click()

    # Go to orders page
    page.get_by_role("button", name='ORDERS').click()
    page.get_by_role("button", name='View').nth(0).click()

    # Validations
    expect(page.locator('body')).to_contain_text('You are not authorize to view this order')
    time.sleep(5)

@pytest.mark.smoke
def test_sessionStorage(playwright: Playwright):

    # Browser init
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # API object
    apiUtils = APIUtils()
    token = apiUtils.getToken(playwright)

    # Test --LOCAL STORAGE--
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/myorders")
    expect(page.locator('body')).to_contain_text('Your Orders')
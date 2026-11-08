from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils


def test_end2endWebAPI(playwright: Playwright):
    # Browser initialization
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Log in
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("eduardwayne1987@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Eduardwayne1987*")
    page.get_by_role("button").click()

    # Create order
    api = APIUtils()
    orderID = api.createOrder(playwright)

    # Validate order
    page.get_by_role("button", name='ORDERS').click()
    orderRow = page.locator("tr").filter(has_text=orderID)
    orderRow.get_by_role("button", name='View').click()
    valMsg = page.locator(".email-preheader")
    expect(valMsg).to_contain_text('Thank you for Shopping With Us')
    context.close()

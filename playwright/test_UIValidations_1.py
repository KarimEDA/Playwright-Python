import time

from playwright.sync_api import Page, expect, Playwright

def test_UIValidationDynamicScript(page: Page):
    # Log in
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="sign in").click()
    # Add items to cart
    item1 = page.locator("app-card").filter(has_text="iphone X")
    item2 = page.locator("app-card").filter(has_text="nokia edge")
    item1.get_by_role("button").click()
    item2.get_by_role("button").click()
    checkOutBtn = page.get_by_text("Checkout")
    expect(checkOutBtn).to_contain_text("2")
    checkOutBtn.click()
    listItems = page.locator(".media-body")
    expect(listItems).to_have_count(2)
    time.sleep(2)

def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with (page.expect_popup() as new_Page):
        #page.locator(".blinkingText").click()
        page.locator(":text('Free Access to InterviewQues/ResumeAssistance/Material')").click()
        page2 = new_Page.value
        email = page2.locator("p.im-para.red")
        expect(email).to_contain_text("mentor@rahulshettyacademy.com")
        time.sleep(5)
        #page2.screenshot(
        #    path="screenshots/fullpage.png",
        #    full_page=True
        #)
        #email = page2.locator("p.im-para.red").text_content()
        #emailAlone = email.split(" ")
        #print(emailAlone[4])
        #assert emailAlone[4] in email

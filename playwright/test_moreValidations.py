import time
from playwright.sync_api import Page, expect, Playwright

def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    text = page.get_by_placeholder("Hide/Show Example")
    text.fill("Hello World")
    expect(text).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(text).to_be_hidden()
    page.expect_console_message()

def test_Alert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog:dialog.dismiss())
    alert = page.locator("#confirmbtn")
    alert2 = page.locator("#alertbtn")
    alert.click()
    alert2.click()

def test_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame1 = page.frame_locator("#courses-iframe")
    frame1.get_by_role("link", name="All Access plan").click()
    expect(frame1.locator(".content-side")).to_contain_text("Happy Subscibers!")

def test_tables(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            colValue = i
            break
    ricePrice = page.locator("tr").filter(has_text="Rice").locator("td").nth(colValue)
    expect(ricePrice).to_contain_text("37")

def test_mouseHover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
    time.sleep(2)




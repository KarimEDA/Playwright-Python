import time
from playwright.sync_api import Page, expect, Playwright
import pytest

@pytest.mark.skip
def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=True)
    # Incognito mode so there is no cache or cookies saved, every operation will be performed
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")

@pytest.mark.skip
def test_FirefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=True)
    # Incognito mode so there is no cache or cookies saved, every operation will be performed
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com")

@pytest.mark.skip
# Chromium in headless shortcut
def test_playwrightShortCut(page: Page):
    page.goto("https://www.rahulshettyacademy.com")

@pytest.mark.skip
def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("incorrect")
    page.get_by_role("combobox").select_option("consult")
    page.get_by_role("link", name="terms and conditions").click()
    page.locator("#terms").check()
    #print(page.pick_locator())
    #page.get_by_role("checkbox").click()
    page.get_by_role("button",name="sign in").click()
    errorMsg = page.get_by_text("Incorrect username/password.")
    print(errorMsg)
    expect(errorMsg).to_be_visible()
    #assert "Incorrect username/password." in errorMsg
    #time.sleep(5)
    # CCS Selector -> id #, class .

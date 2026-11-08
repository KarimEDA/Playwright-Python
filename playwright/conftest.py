from playwright.sync_api import Playwright
import pytest
from pathlib import Path

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chromium", help="Select browser")

@pytest.fixture
def shared_data():
    return {}

@pytest.fixture(scope="function")
def browserInit(playwright: Playwright, request):
    browserName = request.config.getoption("browser_name")
    if browserName == "firefox":
        browser = playwright.firefox.launch(headless=True)
    else:
        browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def contextInit(browserInit):
    context = browserInit.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def pageInit(contextInit):
    page = contextInit.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def user_credentials(request):
    credentials = request.param
    return credentials

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("pageInit")
        if page is not None and not page.is_closed():
            folder = Path("screenshots")
            folder.mkdir(exist_ok=True)
            path = folder / f"{item.name}.png"
            page.screenshot(
                path=str(path),
                full_page=True
            )
            print(f"\nScreenshot generado: {path}")
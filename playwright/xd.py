def test_screenshot(page):
    page.goto("https://www.saucedemo.com/")

    assert page.title() == "Titulo incorrecto"
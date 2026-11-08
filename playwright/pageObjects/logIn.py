from pageObjects.dashboard import dashboardPage

class logInPage:
    def __init__(self, page, pwd):
        self.page = page
        self.pwd = pwd

    def goToLoginPage(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def logIn(self, username):
        self.page.get_by_placeholder("email@example.com").fill(username)
        self.page.get_by_placeholder("enter your passsword").fill(self.pwd)
        self.page.get_by_role("button").click()
        return dashboardPage(self.page)
from playwright.sync_api import expect

class orderDetailsPage:
    def __init__(self, page):
        self.page = page

    def validation(self):
        valMsg = self.page.locator(".email-preheader")
        expect(valMsg).to_contain_text('Thank you for Shopping With Us')
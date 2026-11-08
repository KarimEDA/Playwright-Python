from pageObjects.orderDetails import orderDetailsPage


class ordersHistoryPage:
    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderID):
        orderRow = self.page.locator("tr").filter(has_text=orderID)
        orderRow.get_by_role("button", name='View').click()
        return orderDetailsPage(self.page)
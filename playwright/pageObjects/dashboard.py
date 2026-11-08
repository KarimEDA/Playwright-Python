from pageObjects.ordersHistory import ordersHistoryPage

class dashboardPage:
    def __init__(self, page):
        self.page = page

    def goToOrders(self):
        self.page.get_by_role("button", name='ORDERS').click()
        return ordersHistoryPage(self.page)
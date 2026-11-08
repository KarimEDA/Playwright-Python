from playwright.sync_api import Playwright

payloadOrder = {"orders": [{"country": "Mexico","productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

class APIUtils:

    def getToken(self, playwright: Playwright, username, pwd):
        context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = context.post("/api/ecom/auth/login",
                                data={"userEmail": username,"userPassword": pwd},
                                headers={"Content-Type": "application/json"})
        assert response.ok
        token = response.json()["token"]
        return token

    def createOrder(self, playwright: Playwright, username, pwd):
        token = self.getToken(playwright, username, pwd)
        context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = context.post("/api/ecom/order/create-order", data=payloadOrder,
                     headers={"Authorization": token, "Content-Type": "application/json"})
        assert response.ok
        orderID = response.json()["orders"][0]
        return orderID

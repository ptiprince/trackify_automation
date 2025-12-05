from pages.BasePage import BasePage
from playwright.sync_api import Page

class LogoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logout_button = "#logout-btn"
        self.login_url = "http://127.0.0.1:5500/login.html"

    def logout(self):
        self.click(self.logout_button)
        self.page.wait_for_url(self.login_url)

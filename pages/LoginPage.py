from playwright.sync_api import Page
from .BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = "#email"
        self.password_input = "#password"
        self.login_button = "#login-btn"
        self.login_url = "http://127.0.0.1:5500/login.html"

    def open(self):
        self.open_url(self.login_url)

    def login(self, email, password):
        self.type(self.email_input, email)
        self.type(self.password_input, password)
        self.click(self.login_button)

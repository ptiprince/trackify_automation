from pages.BasePage import BasePage
from playwright.sync_api import Page

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header = "h1"  # Dashboard header selector

    def is_loaded(self):
        # Verify that dashboard header has correct text
        return self.page.inner_text(self.header) == "Dashboard"

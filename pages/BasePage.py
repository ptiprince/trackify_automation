from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # Open any URL
    def open_url(self, url: str):
        self.page.goto(url)

    # Type into input field
    def type(self, selector: str, text: str):
        self.page.fill(selector, text)

    # Click any element
    def click(self, selector: str):
        self.page.click(selector)

    # Wait for URL to match pattern
    def wait_for_url(self, url: str):
        self.page.wait_for_url(url)

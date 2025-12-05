from playwright.sync_api import sync_playwright
import pytest

from config import Config


@pytest.fixture
def browser_page():
    """Create Playwright page and close browser after test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=Config.HEADLESS,
            slow_mo=Config.SLOW_MO,
        )
        page = browser.new_page()
        yield page
        browser.close()

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        yield page
        browser.close()

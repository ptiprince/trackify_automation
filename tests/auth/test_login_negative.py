from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from fixtures.browser_page import browser_page
from config import Config


def test_login_negative(browser_page):
    page = browser_page

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Step 1: open login page
    login_page.open()

    # Step 2: try login with invalid credentials
    login_page.login(Config.INVALID_EMAIL, Config.INVALID_PASSWORD)

    # Step 3: wait a bit and verify we are NOT redirected to dashboard
    page.wait_for_timeout(Config.DEFAULT_TIMEOUT)
    assert "dashboard.html" not in page.url
    assert not dashboard_page.is_loaded()

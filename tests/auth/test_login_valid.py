from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from fixtures.browser_page import browser_page
from config import Config


def test_login_valid(browser_page):
    page = browser_page

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Step 1: open login page
    login_page.open()

    # Step 2: login with valid credentials
    login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)

    # Step 3: wait for dashboard and verify it is loaded
    page.wait_for_url("**/dashboard.html")
    assert dashboard_page.is_loaded()

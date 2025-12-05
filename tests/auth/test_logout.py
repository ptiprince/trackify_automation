from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from pages.LogoutPage import LogoutPage
from fixtures.browser_page import browser_page
from config import Config


def test_logout(browser_page):
    page = browser_page

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    logout_page = LogoutPage(page)

    # Step 1: login
    login_page.open()
    login_page.login(Config.VALID_EMAIL, Config.VALID_PASSWORD)
    page.wait_for_url("**/dashboard.html")
    assert dashboard_page.is_loaded()

    # Step 2: logout
    logout_page.logout()

    # Step 3: verify we are back on login page
    page.wait_for_url("**/login.html")
    assert "login.html" in page.url

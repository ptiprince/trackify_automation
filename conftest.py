import os
import subprocess
import signal
import time
import pytest
from playwright.sync_api import sync_playwright


# ===============================
#  Auto-start local web server
# ===============================

@pytest.fixture(scope="session", autouse=True)
def start_local_server():
    """Start local HTTP server before the test session and stop after."""
    
    project_root = os.path.dirname(os.path.abspath(__file__))
    web_dir = os.path.join(project_root, "web")

    server = subprocess.Popen(
        ["python3", "-m", "http.server", "5500", "--directory", web_dir],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )

    time.sleep(1)  # Ensure server is ready

    yield

    # Kill server
        # Kill server
    try:
        os.killpg(os.getpgid(server.pid), signal.SIGTERM)
    except ProcessLookupError:
        pass


# ===============================
#  Playwright fixtures
# ===============================

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture()
def page(playwright_context):
    page = playwright_context.new_page()
    yield page
    page.close()

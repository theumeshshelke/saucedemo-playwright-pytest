import pytest

from config import PASSWORD, STANDARD_USER
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    """Open the login page and return its page object."""
    lp = LoginPage(page)
    lp.open()
    return lp


@pytest.fixture
def inventory_page(login_page):
    """Log in as a standard user and return the inventory page object."""
    return login_page.login(STANDARD_USER, PASSWORD)

@pytest.fixture(autouse=True)
def slow_network_timeouts(page):
    page.set_default_navigation_timeout(90000)
    page.set_default_timeout(45000)
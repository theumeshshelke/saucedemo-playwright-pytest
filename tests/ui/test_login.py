import pytest
from playwright.sync_api import expect

from config import PASSWORD, STANDARD_USER


@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login(login_page):
    inventory = login_page.login(STANDARD_USER, PASSWORD)
    expect(inventory.title).to_have_text("Products")
    expect(inventory.page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "user, pwd, expected_error",
    [
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", PASSWORD, "Username is required"),
        (STANDARD_USER, "", "Password is required"),
        ("locked_out_user", PASSWORD, "this user has been locked out"),
    ],
    ids=["wrong-password", "empty-username", "empty-password", "locked-out-user"],
)
def test_invalid_login(login_page, user, pwd, expected_error):
    login_page.login(user, pwd)
    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text(expected_error)


@pytest.mark.regression
@pytest.mark.ui
def test_logout(inventory_page):
    inventory_page.logout()
    expect(inventory_page.page).to_have_url("https://www.saucedemo.com/")


@pytest.mark.regression
@pytest.mark.ui
def test_cannot_open_inventory_without_login(page):
    page.goto("/inventory.html")
    expect(page.locator('[data-test="error"]')).to_contain_text("only access '/inventory.html' when you are logged in")

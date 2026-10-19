import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


@pytest.mark.smoke
@pytest.mark.ui
def test_add_item_updates_cart_badge(inventory_page):
    inventory_page.add_to_cart(BACKPACK)
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.regression
@pytest.mark.ui
def test_add_two_items_and_remove_one(inventory_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.add_to_cart(BIKE_LIGHT)
    expect(inventory_page.cart_badge).to_have_text("2")
    inventory_page.remove_from_cart(BACKPACK)
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.regression
@pytest.mark.ui
def test_cart_shows_added_item(inventory_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    cart = CartPage(inventory_page.page)
    assert cart.item_names() == ["Sauce Labs Backpack"]


@pytest.mark.smoke
@pytest.mark.ui
def test_complete_checkout_flow(inventory_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    CartPage(inventory_page.page).checkout()

    checkout = CheckoutPage(inventory_page.page)
    checkout.fill_details("Umesh", "Shelke", "444601")
    checkout.finish()

    expect(checkout.complete_header).to_have_text("Thank you for your order!")


@pytest.mark.regression
@pytest.mark.ui
@pytest.mark.parametrize(
    "first, last, postal, expected_error",
    [
        ("", "Shelke", "444601", "First Name is required"),
        ("Umesh", "", "444601", "Last Name is required"),
        ("Umesh", "Shelke", "", "Postal Code is required"),
    ],
    ids=["no-first-name", "no-last-name", "no-postal-code"],
)
def test_checkout_form_validation(inventory_page, first, last, postal, expected_error):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()
    CartPage(inventory_page.page).checkout()

    checkout = CheckoutPage(inventory_page.page)
    checkout.fill_details(first, last, postal)
    expect(checkout.error).to_contain_text(expected_error)

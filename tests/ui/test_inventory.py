import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.ui
def test_six_products_are_listed(inventory_page):
    expect(inventory_page.items).to_have_count(6)


@pytest.mark.regression
@pytest.mark.ui
def test_sort_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.price_values()
    assert prices == sorted(prices)


@pytest.mark.regression
@pytest.mark.ui
def test_sort_price_high_to_low(inventory_page):
    inventory_page.sort_by("hilo")
    prices = inventory_page.price_values()
    assert prices == sorted(prices, reverse=True)


@pytest.mark.regression
@pytest.mark.ui
def test_sort_name_z_to_a(inventory_page):
    inventory_page.sort_by("za")
    names = inventory_page.product_names()
    assert names == sorted(names, reverse=True)

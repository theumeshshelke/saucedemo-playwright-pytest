from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.items = page.locator('[data-test="inventory-item"]')
        self.prices = page.locator('[data-test="inventory-item-price"]')
        self.names = page.locator('[data-test="inventory-item-name"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator('[data-test="logout-sidebar-link"]')

    def add_to_cart(self, product_slug: str):
        """product_slug example: 'sauce-labs-backpack'"""
        self.page.locator(f'[data-test="add-to-cart-{product_slug}"]').click()

    def remove_from_cart(self, product_slug: str):
        self.page.locator(f'[data-test="remove-{product_slug}"]').click()

    def sort_by(self, value: str):
        """value: az, za, lohi, hilo"""
        self.sort_dropdown.select_option(value)

    def price_values(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def product_names(self) -> list[str]:
        return self.names.all_inner_texts()

    def open_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

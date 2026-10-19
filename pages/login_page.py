from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto("/", wait_until="domcontentloaded")

    def login(self, user: str, pwd: str) -> InventoryPage:
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()
        return InventoryPage(self.page)

    def error_text(self) -> str:
        return self.error.inner_text()

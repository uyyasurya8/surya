import pytest
from playwright.sync_api import Page, expect

def test_add_new_account(page: Page):

    page.goto("https://www.qaplayground.com/bank")
    page.locator('[data-testid="username-input"]').fill("admin")
    page.locator('[data-testid="password-input"]').fill("admin123")
    page.wait_for_timeout(2000)
    page.locator('[data-testid="login-button"]').click()
    expect(page).to_have_url(
    "https://www.qaplayground.com/bank/dashboard"
    )
    page.wait_for_timeout(2000)
    page.locator('[data-testid="quick-add-account"]').click()
    expect(page.get_by_role("heading", name="Add New Account")).to_be_visible()
    page.locator('[data-testid="account-name-input"]').fill("Muhammad Surya Harahap")
    page.wait_for_timeout(3000)
    page.locator('[data-testid="account-type-select"]').first.click()
    page.locator("select").select_option(value="savings", force=True)
    page.keyboard.press("Escape")
    page.locator('[data-testid="initial-balance-input"]').fill("10000000")
    page.locator('[data-testid="save-account-button"]').click()
    expect(page).to_have_url(
    "https://www.qaplayground.com/bank/accounts?action=add"
    )
    print("✅ berhasil menambahkan account")
    page.wait_for_timeout(3000)
    



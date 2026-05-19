import re
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
    page.locator('[data-testid="nav-accounts"]').click()
    page.wait_for_url("https://www.qaplayground.com/bank/accounts")
    page.locator('[data-testid="filter-type-select"]').click()
    page.get_by_text("Savings").click()
    page.wait_for_timeout(2000)
    page.keyboard.press("Escape")
    expect(page.get_by_test_id("account-type").get_by_text("Savings")).to_be_visible()
    print("sukses filter savings")
    page.wait_for_timeout(2000)
    expect(page.get_by_test_id("account-type").get_by_text("Checking")).to_be_hidden()
    print("sukses tidak menampilkan selain saving")
    page.get_by_role("button", name="Reset Filters").click()
    expect(page.locator('[data-column="type"]')).to_be_visible()
    print("sukses mereset filter")
    page.wait_for_timeout(2000)
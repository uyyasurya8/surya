import pytest
from playwright.sync_api import Page, expect


def test_edit_account_name_inline(page: Page):

    # Login
    page.goto("https://www.qaplayground.com/bank")

    page.fill('[data-testid="username-input"]', "admin")
    page.fill('[data-testid="password-input"]', "admin123")
    page.click('[data-testid="login-button"]')

    # Tunggu masuk halaman accounts
    page.locator('[data-testid="nav-accounts"]').click()
    page.wait_for_url("https://www.qaplayground.com/bank/accounts")

    # Tunggu table muncul
    expect(page.locator('[data-testid="accounts-table"]')).to_be_visible()

    # Ambil cell account name pertama
    account_cell = page.locator('[data-testid="account-name"]').first

    # Pastikan belum edit mode
    expect(account_cell).to_have_attribute("data-editing", "false")

    # Simpan nama lama
    old_name = account_cell.inner_text()
    print("Old Name:", old_name)

    # Double click untuk edit
    account_cell.dblclick()

    # Pastikan mode edit aktif
    expect(account_cell).to_have_attribute("data-editing", "true")

    # Input edit muncul
    inline_input = page.locator('[data-testid="inline-edit-input"]')

    expect(inline_input).to_be_visible()
    expect(inline_input).to_be_focused()

    # Isi nama baru
    new_name = "Mansyur X"

    inline_input.fill(new_name)

    # Save dengan Enter
    inline_input.press("Enter")

    # Pastikan input hilang
    expect(inline_input).to_be_hidden()

    # Pastikan text berubah
    expect(account_cell).to_have_text(new_name)

    # Toast sukses muncul
    toast = page.locator("text=Account name updated")
    expect(toast).to_be_visible()


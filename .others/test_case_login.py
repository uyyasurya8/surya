from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    page.goto("https://automationexercise.com/login")
    page.locator('input[data-qa="login-email"]').fill("uyyasurya8@gmail.com")
    page.locator('input[data-qa="login-password"]').fill("Rahasiadong")
    page.locator('button[data-qa="login-button"]').click()
    expect(page.locator("text=Logged in as")).to_be_visible()

print("test_login_success")

def test_login_failed(page: Page):
    page.goto("https://automationexercise.com/login")
    page.locator('input[data-qa="login-email"]').fill("salah@gmail.com")
    page.locator('input[data-qa="login-password"]').fill("12345")
    page.locator('button[data-qa="login-button"]').click()
    expect(page.locator("text=Your email or password is incorrect!")).to_be_visible()

print("test_login_failed")
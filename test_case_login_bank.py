import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
class TestLogin:

    def test_login_success(self, page: Page):

        page.goto("https://www.qaplayground.com/bank")
        page.locator('[data-testid="username-input"]').fill("admin")
        page.locator('[data-testid="password-input"]').fill("admin123")
        page.locator('[data-testid="login-button"]').click()
        expect(page).to_have_url(
        "https://www.qaplayground.com/bank/dashboard"
        )
        page.wait_for_timeout(2000)
        print("✅ Test Login Success Passed")


    def test_login_failed(self, page: Page):

        page.goto("https://www.qaplayground.com/bank")
        page.locator('[data-testid="username-input"]').fill("wrong")
        page.locator('[data-testid="password-input"]').fill("admin123")
        page.locator('[data-testid="login-button"]').click()
        expect(page.locator("text=Invalid username or password")).to_be_visible()
        page.wait_for_timeout(2000)

        print("✅ Test Login Failed")


    def test_login_toogle_pasword_visibility_hides(self, page: Page):

        page.goto("https://www.qaplayground.com/bank")
        password_input = page.locator('[data-testid="password-input"]')
        password_input.fill("admin123")
        expect(password_input).to_have_attribute("type", "password")
        toggle_button = page.locator('[data-testid="toggle-password-btn"]')
        toggle_button.click()
        page.wait_for_timeout(2000)
        expect(password_input).to_have_attribute("type","text" )
        toggle_button.click()
        page.wait_for_timeout(2000)
        expect(password_input).to_have_attribute("type","password")
        page.wait_for_timeout(2000)

        print("✅ Test login with toggle password visibility hides")


    def test_login_success_tanpa_klik_login_button(self, page: Page):

        page.goto("https://www.qaplayground.com/bank")
        page.locator('[data-testid="username-input"]').fill("admin")
        page.locator('[data-testid="password-input"]').fill("admin123")
        page.locator('[data-testid="password-input"]').press("Enter")
        expect(page).to_have_url(
            "https://www.qaplayground.com/bank/dashboard"
        )
        page.wait_for_timeout(2000)

        print("✅ Test Login Success without click login button Passed")

    def test_login_success_akun_read_only(self, page: Page):

        page.goto("https://www.qaplayground.com/bank")
        page.locator('[data-testid="username-input"]').fill("viewer")
        page.locator('[data-testid="password-input"]').fill("viewer123")
        page.locator('[data-testid="login-button"]').click()
        expect(page.locator('data-testid="viewer-badge")'))
        page.wait_for_timeout(2000)

        print("✅ Test Login Success with read only account Passed")
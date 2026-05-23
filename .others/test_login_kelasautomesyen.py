from playwright.sync_api import sync_playwright, expect
import pytest

data_error_login = [('uno.testing3@gmail.com','salah','Invalid login credentials'),
                    ('uno.testing3@gmail.co','1234567890','Invalid login credentials')]

@pytest.mark.parametrize('username , password , error', data_error_login)
def test_login_negative(username , password , error):
    with sync_playwright () as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
       
        page.goto(url='https://test.kelasotomesyen.com/',timeout=10000)
        page.locator('[data-testid="login-email-input"]').fill(username)
        page.locator('[data-testid="login-password-input"]').fill(password)
        page.locator('[data-testid="login-submit-button"]').click()
        
        expect(page).to_have_url('https://test.kelasotomesyen.com/login')
        title = page.title()
        assert title == 'Kelas Otomesyen Test App'

        expect(page.locator('[data-testid="login-error"]')).to_be_visible()
        error_message = page.locator('[data-testid="login-error"]').inner_text()

        assert error_message == error
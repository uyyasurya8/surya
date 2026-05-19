from playwright.sync_api import sync_playwright, expect

def test_add_product():
    with sync_playwright () as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
       
        page.goto(url='https://test.kelasotomesyen.com/')
        page.locator('[data-testid="login-email-input"]').fill("uno.testing3@gmail.com")
        page.locator('[data-testid="login-password-input"]').fill("1234567890")
        page.locator('[data-testid="login-submit-button"]').click()
        page.wait_for_url("https://test.kelasotomesyen.com/products")
        page.locator('[data-testid="add-product-button"]').click()
        page.locator('[data-testid="product-name-input"]').fill("Surya Testing Product 1")
        page.locator('[data-testid="product-price-input"]').fill("2000")
        page.locator('[data-testid="product-stock-input"]').fill("4")
        page.locator('[data-testid="product-category-input"]').select_option(value="Other")
        page.locator('[data-testid="product-description-input"]').fill("testing add product")
        page.locator('[data-testid="submit-button"]').click()
        page.locator('[data-testid="add-product-button"]').click()
        page.locator('[data-testid="product-name-input"]').fill("Surya Testing Product 2")
        page.locator('[data-testid="product-price-input"]').fill("2000")
        page.locator('[data-testid="product-stock-input"]').fill("4")
        page.locator('[data-testid="product-category-input"]').select_option(value="Other")
        page.locator('[data-testid="product-description-input"]').fill("testing add product")
        page.locator('[data-testid="submit-button"]').click()
        page.locator('[data-testid="add-product-button"]').click()
        page.locator('[data-testid="product-name-input"]').fill("Surya Testing Product 3")
        page.locator('[data-testid="product-price-input"]').fill("2000")
        page.locator('[data-testid="product-stock-input"]').fill("4")
        page.locator('[data-testid="product-category-input"]').select_option(value="Other")
        page.locator('[data-testid="product-description-input"]').fill("testing add product")
        page.locator('[data-testid="submit-button"]').click()
        # expect(page.get_by_text("Surya Testing Product").first).to_be_visible()
       
        print("Product Surya berhasil ditambahkan")
        page.wait_for_timeout(5000)

        browser.close()




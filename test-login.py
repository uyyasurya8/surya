# import  asyncio
# from playwright.async_api import async_playwright
# import time

# async def test():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()

#         await page.goto("https://automationexercise.com/signup")

#         await page.locator('input[data-qa="login-email"]').fill("uyyasurya8@gmail.com")
#         await asyncio.sleep(2)
#         await page.locator('input[data-qa="login-password"]').fill("Rahasiadong")
#         await asyncio.sleep(2)
#         async with page.expect_navigation():
#             await page.click('button[data-qa="login-button"]')

#         print("Alamat Website:", page.url)
#         print("Berhasil Login")

#         await page.locator('a[href="/products"]').click()
#         print("Berhasil ke halaman product")
#         await page.locator('a[href="/product_details/4"]').click()
#         print("Berhasil ke halamana product detail")
#         await page.locator('input[name="quantity"]').fill("2")
#         await page.get_by_role("button", name="Add to cart").click()
#         print("Berhasil menambahkan product ke keranjang")
#         await page.get_by_role("button", name="Continue Shopping").click()
        
#         await page.goto("https://automationexercise.com/view_cart")
#         print("Berhasil ke halaman cart")
#         await page.locator('.btn.btn-default.check_out', has_text= " Proceed to Checkout").click()
#         await asyncio.sleep(2)
#         print("Berhasil ke halaman checkout")
#         await page.locator('.form-control').fill("ini testing doang")
#         await asyncio.sleep(2)
#         print("Berhasil coment tentang orderan yang di order")
        
#         async with page.expect_navigation():
#            await page.locator('.btn.btn-default.check_out' , has_text= "Place Order").click()

#         await page.locator('input[data-qa="name-on-card"]').fill("Mansyur X")
#         await page.locator('input[data-qa="card-number"]').fill("1234567890")
#         await page.locator('input[data-qa="cvc"]').fill("311")
#         await page.locator('input[data-qa="expiry-month"]').fill("10")
#         await page.locator('input[data-qa="expiry-year"]').fill("2030")
#         async with page.expect_navigation():
#             await page.locator('.btn.btn-primary.submit-button', has_text= "Pay and Confirm Order").click()

#         print("Transaksi Order Sukses di buat")
#         async with page.expect_download () as download_info:
#             await page.click('xpath=//*[@id="form"]/div/div/div/a')

#         download = await download_info.value
#         await download.save_as("C:/Users/USER/Downloads/"+ download.suggested_filename)

#         await asyncio.sleep(10)

#         print("Berhasil downlaod invoice ke dalam folder")
#         await browser.close()
# asyncio.run(test())        


import asyncio
from playwright.async_api import async_playwright


async def login(page):
    await page.goto("https://automationexercise.com/login")

    await page.locator('[data-qa="login-email"]').fill("uyyasurya8@gmail.com")
    await asyncio.sleep(2)

    await page.locator('[data-qa="login-password"]').fill("Rahasiadong")
    await asyncio.sleep(2)

    async with page.expect_navigation():
        await page.locator('[data-qa="login-button"]').click()

    print("✅ Berhasil Login")
    print("🌐 URL:", page.url)


async def add_product_to_cart(page):
    await page.locator('a[href="/products"]').click()
    print("✅ Berhasil ke halaman product")

    await page.locator('a[href="/product_details/4"]').click()
    print("✅ Berhasil ke halaman detail product")

    await page.locator('input[name="quantity"]').fill("2")

    await page.get_by_role("button", name="Add to cart").click()
    print("✅ Product berhasil ditambahkan ke cart")

    await page.get_by_role("button", name="Continue Shopping").click()


async def checkout_product(page):
    await page.goto("https://automationexercise.com/view_cart")
    print("✅ Berhasil ke halaman cart")

    await page.locator('.btn.btn-default.check_out').click()
    await asyncio.sleep(2)

    print("✅ Berhasil ke halaman checkout")

    await page.locator('.form-control').fill("Ini testing order automation")
    print("✅ Berhasil input komentar order")

    async with page.expect_navigation():
        await page.locator('.btn.btn-default.check_out').click()


async def payment_process(page):
    await page.locator('[data-qa="name-on-card"]').fill("Mansyur X")
    await page.locator('[data-qa="card-number"]').fill("1234567890")
    await page.locator('[data-qa="cvc"]').fill("311")
    await page.locator('[data-qa="expiry-month"]').fill("10")
    await page.locator('[data-qa="expiry-year"]').fill("2030")

    async with page.expect_navigation():
        await page.locator('.btn.btn-primary.submit-button').click()

    print("✅ Transaksi order sukses")


async def download_invoice(page):
    async with page.expect_download() as download_info:
        await page.click('xpath=//*[@id="form"]/div/div/div/a')

    download = await download_info.value

    await download.save_as(
        "C:/Users/USER/Downloads/" + download.suggested_filename
    )

    print("✅ Invoice berhasil di-download")


async def main():
    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        page = await browser.new_page()

        # LOGIN
        await login(page)

        # ADD PRODUCT
        await add_product_to_cart(page)

        # CHECKOUT
        await checkout_product(page)

        # PAYMENT
        await payment_process(page)

        # DOWNLOAD INVOICE
        await download_invoice(page)

        await asyncio.sleep(5)

        await browser.close()


asyncio.run(main())
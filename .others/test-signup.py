# import asyncio
# from playwright.async_api import async_playwright
# import time

# async def test():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto("https://automationexercise.com/login")
#         await page.locator('input[data-qa="signup-name"]').fill("MansyurX")
#         await page.locator('input[data-qa="signup-email"]').fill("MansyurX@gmail.com")
#         time.sleep(5)
#         await page.click('button[type="submit"]').click()
#         time.sleep(5)
#         await browser.close()
# asyncio.run(test())


import asyncio
from playwright.async_api import async_playwright
import time

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://automationexercise.com/login")

        await page.locator('input[data-qa="signup-name"]').fill("uyya")
        await asyncio.sleep(2)
        await page.locator('input[data-qa="signup-email"]').fill("uyyasurya8@gmail.com")
        await asyncio.sleep(2)
      
        async with page.expect_navigation():
            await page.click('button[data-qa="signup-button"]')

        print("Alamat Website:", page.url)

        await page.wait_for_url("https://automationexercise.com/signup")
        print("Berhasil ke halaman signup")
        await page.locator('#id_gender1').check() 
        await page.locator("input.form-control[type='password']").fill("Rahasiadong")
        await page.locator('select[data-qa="days"]').select_option("10")
        await page.locator('select[data-qa="months"]').select_option("7")
        await page.locator('select[data-qa="years"]').select_option("1990")
        await page.locator('input[name="newsletter"]').check()
        await page.locator('input[data-qa="first_name"]').fill("Kaif")
        await page.locator('input[data-qa="last_name"]').fill("Harahap")
        await page.locator('input[data-qa="company"]').fill("Bank Sinarmas")
        await page.locator('input[data-qa="address"]').fill("Jalan Raya Cikaret Gang SUkamanh 4 ")
        await page.locator('input[data-qa="address"]').fill("rt 3 rw 10 no.43 pakansari cibinong")
        await page.locator('select[data-qa="country"]').select_option("Canada")
        await page.locator('input[data-qa="state"]').fill("JAWA BARAT")
        await page.locator('input[data-qa="city"]').fill("Bogor")
        await page.locator('input[data-qa="zipcode"]').fill("16915")
        await page.locator('input[data-qa="mobile_number"]').fill("081287858594")
        async with page.expect_navigation():
            await page.click('button[data-qa="create-account"]')

        print("Berhasil create account")
        await asyncio.sleep(2)
        await browser.close()

asyncio.run(test())



# from playwright.sync_api import sync_playwright
# import time

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://google.com")
#     print(page.title)
#     time.sleep(10)
#     browser.close()
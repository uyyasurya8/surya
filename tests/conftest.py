from playwright.sync_api import sync_playwright 
import pytest


@pytest.fixture
def browser():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://test.kelasotomesyen.com/",timeout=10000)

        yield page

        browser.close()
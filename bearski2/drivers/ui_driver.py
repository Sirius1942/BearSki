"""UI 驱动 - Playwright"""
from playwright.sync_api import sync_playwright

class UIDriver:
    def __init__(self, session):
        self.session = session
        if not self.session.ui_browser:
            self.playwright = sync_playwright().start()
            self.session.ui_browser = self.playwright.chromium.launch()
            self.page = self.session.ui_browser.new_page()
    
    def open(self, url):
        self.page.goto(url)
    
    def input(self, selector, value):
        self.page.locator(selector).fill(value)
    
    def click(self, selector):
        self.page.locator(selector).click()
    
    def get_text(self, selector):
        return self.page.locator(selector).text_content()
    
    def assert_text(self, selector, expected):
        actual = self.get_text(selector)
        assert expected in actual, f"Expected '{expected}' in '{actual}'"

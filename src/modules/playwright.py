from src.modules.base import BaseModule
from playwright.sync_api import sync_playwright as pw
from playwright.sync_api import Browser, Page
from typing import Optional, List

PW = pw()
browser: Optional[Browser] = None
page: List[Page] = []
cur_page: Optional[Page] = None


class BrowserOpenUrl(BaseModule):
    id = "browser_open_url"
    name = "Browser Open Url"
    version = "0.0.1"

    def run(self, url: str):
        global PW
        global browser
        global page
        global cur_page
        print(url)
        browser = PW.start().chromium.launch(headless=False)
        page.append(browser.new_page())
        cur_page = page[0]
        cur_page.goto(url)


class BrowserClick(BaseModule):
    id = "browser_click"
    name = "Browser Click"
    version = "0.0.1"

    def run(self, selector: str):
        global PW
        global browser
        global page
        global cur_page
        cur_page.click(selector)


class BrowserDoubleClick(BaseModule):
    id = "browser_double_click"
    name = "Browser Double Click"
    version = "0.0.1"
    description = "鼠标双击元素"

    def run(self, selector: str):
        global PW
        global browser
        global page
        global cur_page
        cur_page.dblclick(selector)


class BrowserInput(BaseModule):
    id = "browser_input"
    name = "Browser Input"
    version = "0.0.1"

    def run(self, selector: str, text: str):
        global PW
        global browser
        global page
        global cur_page
        cur_page.fill(selector, text)


class BrowserClose(BaseModule):
    id = "browser_close"
    name = "Browser Close"
    version = "0.0.1"

    def run(self):
        global PW
        global browser
        global page
        global cur_page
        browser.close()

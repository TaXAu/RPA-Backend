from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time


def init_chrome(headless=False):
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


def init_firefox(headless=False):
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver


def init_ie(headless=False):
    from webdriver_manager.microsoft import IEDriverManager
    driver = webdriver.Ie(service=Service(IEDriverManager().install()))
    return driver


def init_opera(headless=False):
    from webdriver_manager.opera import OperaDriverManager
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    return driver


def init_edge(headless=False):
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    return driver


def init_chromium(headless=False):
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.utils import ChromeType
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    return driver


# class Selector:
#     type_list = ["id", "name", "class", "tag", "link", "xpath", "css"]
#
#     def __init__(self, **kwargs):
#         self.type =
#         self.type_no = self.type_list.index(self.type)


class RpaBrowser:
    browsers = {'chrome': init_chrome,
                'firefox': init_firefox,
                'ie': init_ie,
                'opera': init_opera,
                'edge': init_edge,
                'chromium': init_chromium}
    instance = []

    def __init__(self, browser_type, headless=False):
        if browser_type in RpaBrowser.browsers:
            self.driver = RpaBrowser.browsers[browser_type](headless)
            self.pages = []
        else:
            raise Exception('Browser type not supported')

    def url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def select(self, type, selector):
        el = None

        if type == 'id':
            el = self.driver.find_element(By.ID, selector)
        elif type == 'xpath':
            el = self.driver.find_element(By.XPATH, selector)
        elif type == 'css':
            el = self.driver.find_element(By.CSS_SELECTOR, selector)
        elif type == 'name':
            el = self.driver.find_element(By.NAME, selector)
        elif type == 'class':
            el = self.driver.find_element(By.CLASS_NAME, selector)
        else:
            raise Exception('Selector type not supported')

        return el

    def input(self, type, selector, text):
        el = self.select(type, selector)
        el.send_keys(text)

    def click(self, type, selector):
        el = self.select(type, selector)
        el.click()


# def open_browser(*args, **kwargs):
#     # options = se.webdriver.ChromeOptions()
# 
#     print("Open Browser: ", args, kwargs)
#     # r.init()
# 
# 
# def open_url(*args, **kwargs):
#     print("Open URL: ", args, kwargs)
#     if "url" in kwargs:
#         r.url(kwargs.url)
# 
# 
# def input_text(*args, **kwargs):
#     print("Input Text: ", args, kwargs)
#
#
# def click_button(*args, **kwargs):
#     print("Click Button: ", args, kwargs)
#
#
# def close_browser(*args, **kwargs):
#     print("Close Browser: ", args, kwargs)

easy_browser = None


def easy_open_browser(browser_type="chrome", headless=False, **kwargs):
    global easy_browser
    easy_browser = RpaBrowser(browser_type, headless)


def easy_open_url(url, **kwargs):
    easy_browser.url(url)


def easy_input_text(type, selector, text, **kwargs):
    easy_browser.input(type, selector, text)


def easy_click_button(type, selector, **kwargs):
    easy_browser.click(type, selector)


def easy_close_browser(**kwargs):
    easy_browser.close()


def delay(seconds, **kwargs):
    time.sleep(int(seconds))


# web_functions = {"open_browser": open_browser,
#                  "open_url": open_url,
#                  "input_text": input_text,
#                  "click_button": click_button,
#                  "close_browser": close_browser}

web_functions_easy = {
    "open_browser": easy_open_browser,
    "open_url": easy_open_url,
    "input_text": easy_input_text,
    "click_button": easy_click_button,
    "close_browser": easy_close_browser,
    "delay": delay
}

web_functions = {"open_browser": RpaBrowser,
                 "open_url": RpaBrowser.url,
                 "input_text": RpaBrowser.input,
                 "click_button": RpaBrowser.click,
                 "close_browser": RpaBrowser.close}

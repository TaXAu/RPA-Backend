from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time


# init browser


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

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    )
    return driver


# end init browser


def if_support(browser_type):
    if browser_type in Browser.browsers:
        return True
    else:
        return False


class Browser:
    # All supported browsers
    browsers = {
        "chrome": init_chrome,
        "firefox": init_firefox,
        "ie": init_ie,
        "opera": init_opera,
        "edge": init_edge,
        "chromium": init_chromium,
    }
    instance = []  # list of browser instances

    def __init__(self, **kwargs):
        if "browser_type" in kwargs:
            if kwargs["browser_type"] in self.browsers:
                self.browser_type = kwargs["browser_type"]
                self.driver = self.browsers[self.browser_type]()
                self.instance.append(self)
            else:
                raise Exception("Browser type not supported")
        else:
            print("Init without a browser.")

    def __del__(self):
        try:
            self.__driver().close()
        except AttributeError:
            pass

    def __driver(self):
        try:
            return self.driver
        except AttributeError:
            if len(Browser.instance) > 0:
                return Browser.instance[0].driver
            else:
                raise Exception("No browser instance")

    def new_instance(self, browser_type="edge", headless=False, **kwargs):
        if if_support(browser_type):
            Browser(browser_type=browser_type, headless=headless, **kwargs)
        else:
            raise Exception("Browser type not supported")

    def url(self, url, **kwargs):
        self.__driver().get(url)

    def close(self, **kwargs):
        self.__del__()

    def select(self, type, selector, **kwargs):
        el = None

        if type == "id":
            el = self.__driver().find_element(By.ID, selector)
        elif type == "xpath":
            el = self.__driver().find_element(By.XPATH, selector)
        elif type == "css":
            el = self.__driver().find_element(By.CSS_SELECTOR, selector)
        elif type == "name":
            el = self.__driver().find_element(By.NAME, selector)
        elif type == "class":
            el = self.__driver().find_element(By.CLASS_NAME, selector)
        else:
            raise Exception("Selector type not supported")

        return el

    def input(self, type, selector, text, **kwargs):
        el = self.select(type, selector)
        el.send_keys(text)

    def click(self, type, selector, **kwargs):
        el = self.select(type, selector)
        el.click()


web_functions = {
    "open_browser": Browser,
    "open_url": Browser.url,
    "input_text": Browser.input,
    "click_button": Browser.click,
    "close_browser": Browser.close,
}

# Easy mode of web automation
# Which means there is only one global browser instance

easy_browser = Browser()


def delay(seconds, **kwargs):
    time.sleep(int(seconds))


web_functions_easy = {
    "open_browser": easy_browser.new_instance,
    "open_url": easy_browser.url,
    "input_text": easy_browser.input,
    "click_button": easy_browser.click,
    "close_browser": easy_browser.close,
    "delay": delay,
}

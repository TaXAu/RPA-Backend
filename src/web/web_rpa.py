def open_browser(*args, **kwargs):
    print("Open Browser: ", args, kwargs)


def open_url(*args, **kwargs):
    print("Open URL: ", args, kwargs)


def input_text(*args, **kwargs):
    print("Input Text: ", args, kwargs)


def click_button(*args, **kwargs):
    print("Click Button: ", args, kwargs)


def close_browser(*args, **kwargs):
    print("Close Browser: ", args, kwargs)


web_functions = {"open-browser": open_browser,
                 "open-url": open_url,
                 "input-text": input_text,
                 "click-button": click_button,
                 "close-browser": close_browser}

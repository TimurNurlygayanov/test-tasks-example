# Note: this is very simple example of conftest.py file
# You should rename this file to conftest.py - PyTest will
# check this file for all fixtures.

import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.binary = '/usr/bin/firefox'
    firefox_options.add_argument('-headless')
    firefox_options.set_preference('dom.disable_beforeunload', True)
    firefox_options.set_preference('browser.tabs.warnOnClose', False)

    return firefox_options


@pytest.fixture(scope="function")
def web_browser(request, selenium):
    browser = selenium
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    yield browser

    try:
        # Close browser window:
        b.quit()
    except:
        pass  # just ignore any errors if we can't close the browser.

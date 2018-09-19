import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_wait_until(web_browser):
    """ This is simple test case shows how to wait until
        some element will be ready for click.
    """

    web_browser.get('https://ya.ru')

    button_xpath = '//button[contains(@class, "button_theme_websearch")]'
    button = WebDriverWait(web_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath)))

    button.click()

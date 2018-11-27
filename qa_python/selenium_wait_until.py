#!/usr/bin/python3
# -*- encoding=utf8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait_until(selenium):
    """ This is simple test case shows how to wait until
        some element will be ready for click.
    """

    selenium.get('https://ya.ru')

    button_xpath = '//button[contains(@class, "button_theme_websearch")]'
    button = WebDriverWait(selenium, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

    button.click()

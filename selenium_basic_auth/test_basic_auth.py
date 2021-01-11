# How to run:
# python3 -m pytest -v --driver Chrome --driver-path ~/chrome

import time
import pytest


def test_make_auth(selenium):
    """ This is basic example how to overtake
        basic auth in Selenium tests.
    """

    selenium.get('https://www.httpwatch.com/httpgallery/authentication/')
    button_display_image = selenium.find_element_by_id('displayImage')

    button_display_image.click()

    time.sleep(10)

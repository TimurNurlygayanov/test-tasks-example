#!/usr/bin/python3
# -*- encoding=utf8 -*-

# How to run test:
#    python3 -m pytest -v selenium_upload_file.py --driver Chrome --driver-path /tests/chrome
#

import time


def test_wait_until(selenium):
    """ This is simple test case shows how to wait until
        some element will be ready for click.
    """

    selenium.get('https://yandex.ru/images/search')

    # Click on "Search by image" button:
    button = selenium.find_element_by_xpath('//button[@aria-label="Поиск по картинке"]')
    button.click()

    # Upload image file:
    image_container = selenium.find_element_by_xpath('//input[@type="file"]')
    image_container.send_keys('/images/my_img.png')

    time.sleep(10)    # for demo purposes only, do NOT repeat it
                      # on the real projects!

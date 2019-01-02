#!/usr/bin/python3
# -*- encoding=utf8 -*-

# Here you can find the example of highlighting of element
# before click - it can be very useful for debugging.
#
# How to run test:
#    python3 -m pytest -v highlight_element.py --driver Chrome --driver-path /tests/chrome
#

import uuid


def test(web_browser):
    """ This is very simple example how to highlight
        element before click.
    """

    element = web_browser.find_element_by_id('test')
    # Scroll page to the element:
    web_browser.execute_script("arguments[0].scrollIntoView();", element)
    # Add red border to the style:
    web_browser.execute_script("arguments[0].style.border='3px solid red'", element)
    # Make screen-shot of the page:
    web_browser.save_screenshot('screenshots/{0}.png'.format(uuid.uuid4()))

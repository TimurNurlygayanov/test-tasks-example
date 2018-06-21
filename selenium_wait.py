# Here is the example how to wait while the page will be fully loaded:
#
# So, ok, it is a dirty workaround, but it works well.
# more examples here: https://blog.codeship.com/get-selenium-to-wait-for-page-load/
#

import time


def open_page_simple(web_browser, url):
    """ This is simple function which checks that page loaded completely. """

    web_browser.get(url)

    page_loaded = False

    # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    while not page_loaded:
        time.sleep(1)

        # Scroll down and wait when page will be loaded:
        web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        page_loaded = web_browser.execute_script("return document.readyState == 'complete';")

    # Go up:
    web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')


def open_page(web_browser, url):
    """ This is advanced function which also checks that all images completely loaded. """

    web_browser.get(url)

    page_loaded = False
    images_loaded = False

    script = ("return arguments[0].complete && typeof arguments[0].natural"
              "Width != \"undefined\" && arguments[0].naturalWidth > 0")

    # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    while not page_loaded and not images_loaded:
        time.sleep(1)

        # Scroll down and wait when page will be loaded:
        web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        page_loaded = web_browser.execute_script("return document.readyState == 'complete';")

        # Make sure that every image loaded completely
        # (sometimes we have to scroll to the image to push browser upload it):
        pictures = web_browser.find_elements_by_xpath('//img')
        res = []

        for image in pictures:
            src = image.get_attribute('src')
            if src:
                # Scroll down to each image on the page:
                image.location_once_scrolled_into_view
                web_browser.execute_script("window.scrollTo(0, 155)")

                image_ready = web_browser.execute_script(script, image)

                if not image_ready:
                    # if the image not ready, give it a try to load and check again:
                    time.sleep(5)
                    image_ready = web_browser.execute_script(script, image)

                res.append(image_ready)

        # Check that every image loaded and has some width > 0:
        images_loaded = False not in res

    # Go up:
    web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

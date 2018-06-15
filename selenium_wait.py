# Here is the example how to wait while the page will be fully loaded:
#
# So, ok, it is a dirty workaround, but it works well.
# more examples here: https://blog.codeship.com/get-selenium-to-wait-for-page-load/
#

import time


def open_page(web_browser, url):
    web_browser.get(url)

    # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    for i in range(10):
        time.sleep(1)
        web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        web_browser.execute_script("while (document.readyState != 'complete') {  };")

    # Return back to the beggining of the page:
    web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')

# Note: this code works only with tha latest ALPHA
# version of selenium library & selenium chrome driver.

import selenium
import base64


def test_try_selenium():
    driver = selenium.webdriver.Chrome()
    driver.get('https://www.httpwatch.com/httpgallery/authentication/')

    auth = base64.b64encode(b'user:pass').decode()

    driver.execute_cdp_cmd('Network.enable', {})
    driver.execute_cdp_cmd('Network.setExtraHTTPHeaders',
                           {'headers': {'Proxy-Authorization': 'Basic ' + auth}})

    driver.refresh()

    driver.find_element_by_id('displayImage').click('displayImage')


import os
from appium import webdriver


def set_up():
    capabilities = {
        "browserName": "android",
        "browserVersion": "10.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote('http://localhost:4444/wd/hub', capabilities)


set_up()

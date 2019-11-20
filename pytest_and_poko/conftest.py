import pytest
from airtest.core.api import *
from poco.drivers.std import StdPoco


@pytest.fixture
def device():
    poco = StdPoco()

    auto_setup(__file__)

    # connect an android phone with adb
    init_device("Android")

    PWD = os.path.dirname(__file__)
    PKG = 'io.neurohive.match2'
    APK = os.path.join(PWD, 'Travel-Blast.apk')

    if PKG not in device().list_app():
        install(APK)

    stop_app(PKG)
    wake()
    start_app(PKG)
    sleep(2)

    raise poco

    sleep(2)
    stop_app(PKG)

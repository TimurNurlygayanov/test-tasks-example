import pytest


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.add_extension('basic_auth_plugin')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--load-extension=./basic_auth_plugin')
    return chrome_options

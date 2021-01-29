import os
import pytest


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
EXTENSION_ROOT = os.path.join(PROJECT_ROOT, 'extension')

chrome_options = Options()
chrome_options.add_argument(
    'load-extension={0}'.format(EXTENSION_ROOT)
)

@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.add_extension('basic_auth_plugin')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--load-extension=./basic_auth_plugin')
    return chrome_options

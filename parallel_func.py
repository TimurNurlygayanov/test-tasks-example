import requests
from joblib import Parallel, delayed

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS='ALL'


def check():
    res = requests.get('https://google.com')


TODO = [i for i in range(100)]


# Run function "check" in 10 threads:
Parallel(n_jobs=10, timeout=300, backend='threading') \
        (delayed(check)(task, 'test parameter')
         for task in TODO)

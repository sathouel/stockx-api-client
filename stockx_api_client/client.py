from urllib.parse import urljoin
import requests as rq

from . import (
    resources,
    utils
)

class StockxClient:
    BASE_URL = 'https://stockx.com'
    def __init__(self):
        
        self._session = rq.Session()
        self._session.headers.update({
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        })

        self._resources = {
            'browse': resources.BrowsePool(
                urljoin(self.BASE_URL, 'api/browse'), self._session
            )
        }

    @property
    def resources(self):
        return self._resources

    @property
    def browse(self):
        return self._resources['browse']

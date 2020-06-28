import unittest
from . import apinews

from nstorelogger.logger import Logger
log = Logger()

class TestNewsApi(unittest.TestCase):
    def test_get_news(self):
        log.debug('Running test on NewsAPI get news call')
        listFromApiResponse = apinews.NewsApi('general').getNews()
        for item in listFromApiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source'])
        log.debug('Test ended')
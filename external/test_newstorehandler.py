import unittest
from . import newstorehandler as nh

from nstorelogger.logger import Logger
log = Logger()

class TestRedditApi(unittest.TestCase):
    def test_get_all_news(self):
        log.debug('Running test on all third-party news aggregation')
        listFromApiResponse = nh.NewstoreHandler('general').getAllNews()
        for item in listFromApiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source'])
        log.debug('Test ended')
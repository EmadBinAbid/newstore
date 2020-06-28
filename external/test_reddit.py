import unittest
from . import reddit

from nstorelogger.logger import Logger
log = Logger()

class TestRedditApi(unittest.TestCase):
    def test_get_news(self):
        log.debug('Running test on Reddit API get news call')
        listFromApiResponse = reddit.RedditApi('news').getNews()
        for item in listFromApiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source'])
        log.debug('Test ended')
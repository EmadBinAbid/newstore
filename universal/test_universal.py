import unittest
from .universal import Universal

from nstorelogger.logger import Logger
log = Logger()

class TestUniversal(unittest.TestCase):
    def test_get_news_sources(self):
        log.debug('Running test on get news sources from static in-memory instance')
        self.assertEqual(type(Universal.getNewsSources()), type(dict()))
        log.debug('Test ended')
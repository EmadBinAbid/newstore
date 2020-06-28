import unittest
from .universal import Universal

class TestUniversal(unittest.TestCase):
    def test_get_news_sources(self):
        self.assertEqual(type(Universal.getNewsSources()), type(dict()))
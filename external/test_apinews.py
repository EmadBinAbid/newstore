import unittest
from . import apinews

class TestNewsApi(unittest.TestCase):
    def test_get_news(self):
        listFromApiResponse = apinews.NewsApi('general').getNews()
        for item in listFromApiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source'])
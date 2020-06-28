import unittest
from . import reddit

class TestRedditApi(unittest.TestCase):
    def test_get_news(self):
        listFromApiResponse = reddit.RedditApi('news').getNews()
        for item in listFromApiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source'])
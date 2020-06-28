import unittest
from . import newstorehandler as nh

class TestRedditApi(unittest.TestCase):
    def test_get_all_news(self):
        listFromApiResponse = nh.NewstoreHandler('general').getAllNews()
        for item in listFromApiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source'])
import unittest
from .views import news_list, sources_list, getKeywordId
from .models import News, Keywords, NewsHistory, Sources
from config.appconfig import get_api_token
from rest_framework.test import APIClient

class TestUniversal(unittest.TestCase):
    def test_get_news_list(self):
        # Test with auth
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=get_api_token())
        response = client.get('/news')
        request = response.wsgi_request
        apiResponse = news_list(request)
        apiResponse = apiResponse.data
        for item in apiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source_id_id'])

        # Test without auth
        client = APIClient()
        response = client.get('/news')
        request = response.wsgi_request
        apiResponse = news_list(request)
        self.assertEqual(apiResponse.status_code, 401)

    def test_get_sources_list(self):
        # Test with auth
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=get_api_token())
        response = client.get('/sources')
        request = response.wsgi_request
        apiResponse = sources_list(request)
        apiResponse = apiResponse.data
        for item in apiResponse:
            self.assertEqual(list(item.keys()), ['id', 'source'])

        # Test without auth
        client = APIClient()
        response = client.get('/sources')
        request = response.wsgi_request
        apiResponse = sources_list(request)
        self.assertEqual(apiResponse.status_code, 401)
    
    def test_get_keyword_id(self):
        keywordsList = Keywords.objects.filter(keyword='general').values('id')
        keywordIdList = list()
        for keyword in keywordsList:
            keywordIdList.append(keyword['id'])
        
        self.assertIn(getKeywordId('general'), keywordIdList)
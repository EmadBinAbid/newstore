import unittest
from .views import news_list, sources_list, getKeywordId
from .models import News, Keywords, NewsHistory, Sources
from config.appconfig import get_api_token
from rest_framework.test import APIClient

from nstorelogger.logger import Logger
log = Logger()

class TestApiView(unittest.TestCase):
    def test_get_news_list(self):
        # Test with auth
        log.debug('Running test on GET /news with auth')

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=get_api_token())
        response = client.get('/news')
        request = response.wsgi_request
        apiResponse = news_list(request)
        apiResponse = apiResponse.data
        for item in apiResponse:
            self.assertEqual(list(item.keys()), ['headline', 'link', 'source_id_id'])
        log.debug('Test ended')

        # Test without auth
        log.debug('Running test on GET /news without auth')
        client = APIClient()
        response = client.get('/news')
        request = response.wsgi_request
        apiResponse = news_list(request)
        self.assertEqual(apiResponse.status_code, 401)
        log.debug('Test ended')

    def test_get_sources_list(self):
        # Test with auth
        log.debug('Running test on GET /sources with auth')
        
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=get_api_token())
        response = client.get('/sources')
        request = response.wsgi_request
        apiResponse = sources_list(request)
        apiResponse = apiResponse.data
        for item in apiResponse:
            self.assertEqual(list(item.keys()), ['id', 'source'])
        log.debug('Test ended')

        # Test without auth
        log.debug('Running test on GET /sources without auth')
        client = APIClient()
        response = client.get('/sources')
        request = response.wsgi_request
        apiResponse = sources_list(request)
        self.assertEqual(apiResponse.status_code, 401)
        log.debug('Test ended')
    
    def test_get_keyword_id(self):
        log.debug('Running test for checking valid keyword id')
        keywordsList = Keywords.objects.filter(keyword='general').values('id')
        keywordIdList = list()
        for keyword in keywordsList:
            keywordIdList.append(keyword['id'])
        
        self.assertIn(getKeywordId('general'), keywordIdList)
        log.debug('Test ended')
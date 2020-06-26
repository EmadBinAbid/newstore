from newsapi.newsapi_client import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException

from rest_framework.response import Response

from config.newsapiconfig import get_newsapi_config

newsapiconfig = get_newsapi_config()
api = NewsApiClient(api_key=newsapiconfig['API_KEY'])

class NewsApi:
    def __init__(self, q):
        self.q = q
        self.news = list()
    
    def getNews(self):
        try:
            responseObject = api.get_everything(q=self.q)
            newsList = responseObject['articles']
            for news in newsList:
                self.news.append({
                    'headline': news['title'],
                    'link': news['url'],
                    'source': 'newsapi'
                })

            return self.news
        except NewsAPIException as e:
            raise Exception("NewsAPI Exception: {}.".format(str(e)))
        except Exception as e:
            raise Exception("Newzology Exception: {}.".format(str(e)))
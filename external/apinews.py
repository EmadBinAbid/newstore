from newsapi.newsapi_client import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
from rest_framework.response import Response
from config.newsapiconfig import get_newsapi_config, get_name

newsapiconfig = get_newsapi_config()
api = NewsApiClient(api_key=newsapiconfig['API_KEY'])

class NewsApi:
    def __init__(self, q):
        self.q = q
        self.name = get_name()                                  # Getting name from config for consistency
        self.news = list()
    
    def getNews(self) -> list:
        try:
            responseObject = api.get_everything(q=self.q)       # API call
            newsList = responseObject['articles']
            for news in newsList:
                self.news.append({
                    'headline': news['title'],
                    'link': news['url'],
                    'source': self.name
                })

            return self.news
        except NewsAPIException as e:
            raise Exception("NewsAPI Exception: {}.".format(str(e)))
        except Exception as e:
            raise Exception("Newzology Exception: {}.".format(str(e)))
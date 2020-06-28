from newsapi.newsapi_client import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
from rest_framework.response import Response
from config.newsapiconfig import get_newsapi_config, get_name

from nstorelogger.logger import Logger
log = Logger()

newsapiconfig = get_newsapi_config()
api = NewsApiClient(api_key=newsapiconfig['API_KEY'])

class NewsApi:
    """
    This class handles all the communication with NewsAPI third-party API. 
    In order for this class to function properly, it is expected that a
    valid API_KEY will be set in config.newsapiconfig.py. This class uses
    'newsapi' Python wrapper to hit the requests.
    """

    def __init__(self, q):
        self.q = q
        self.name = get_name()                                  # Getting name from config for consistency
        self.news = list()
    
    def getNews(self) -> list:
        """
        Hits the NewsAPI's '/everthing' endpoint using 'get_everything' wrapper 
        function to fetch all the news from API.

        Parameters:
        None

        Returns: 
        list: a list of dictionary objects containing news from NewsAPI
        
        """
        try:
            responseObject = api.get_everything(q=self.q)       # API call
            newsList = responseObject['articles']
            for news in newsList:
                self.news.append({
                    'headline': news['title'],
                    'link': news['url'],
                    'source': self.name
                })

            log.debug('Fetched data from NewsAPI')
            return self.news
        except NewsAPIException as e:
            log.error('NewsAPI Exception:' + str(e))
            raise Exception("NewsAPI Exception: {}.".format(str(e)))
        except Exception as e:
            log.error('Newstore Exception:' + str(e))
            raise Exception("Newstore Exception: {}.".format(str(e)))
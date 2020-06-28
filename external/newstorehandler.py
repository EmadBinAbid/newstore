from . import apinews, reddit

from nstorelogger.logger import Logger
log = Logger()

class NewstoreHandler:
    """
    This class acts as an aggregator to compile the news from all supported 
    third-party APIs in Newstore. 
    """

    def __init__(self, q):
        self.q = q
        self.apiNews = apinews.NewsApi(self.q)
        self.redditNews = reddit.RedditApi(self.q)

    def getAllNews(self) -> list:
        """
        Aggregates the news from all supported third-party APIs by combining 
        the list of dictionary objects into a single list
        
        Parameters:
        None

        Returns: 
        list: a list of dictionary objects containing news from all third-party APIs
        """
        try:
            allNews = self.apiNews.getNews() + self.redditNews.getNews()
            log.debug('Aggregated responses from all supported third party APIs')
            return allNews
        except Exception as e:
            log.error('Newstore Exception:' + str(e))
            raise Exception("Newstore Exception: {}.".format(str(e)))

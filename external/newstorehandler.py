from . import apinews, reddit

from nstorelogger.logger import Logger
log = Logger()

class NewstoreHandler:
    def __init__(self, q):
        self.q = q
        self.apiNews = apinews.NewsApi(self.q)
        self.redditNews = reddit.RedditApi(self.q)

    def getAllNews(self) -> list:
        try:
            allNews = self.apiNews.getNews() + self.redditNews.getNews()
            log.debug('Aggregated responses from all supported third party APIs')
            return allNews
        except Exception as e:
            log.error('Newstore Exception:' + str(e))
            raise Exception("Newstore Exception: {}.".format(str(e)))

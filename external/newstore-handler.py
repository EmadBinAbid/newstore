from . import apinews, reddit

class NewstoreHandler:
    def __init__(self, q):
        self.q = q
        self.apiNews = apinews.NewsApi(self.q)
        self.redditNews = reddit.RedditApi(self.q)

    def getAllNews(self):
        return self.apiNews + self.redditNews
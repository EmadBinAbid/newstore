import praw
from praw.exceptions import APIException
from rest_framework.response import Response
from config.redditapiconfig import get_redditapi_config, get_name

redditapiconfig = get_redditapi_config()
reddit = praw.Reddit(client_id=redditapiconfig['CLIENT_ID'],
                     client_secret=redditapiconfig['CLIENT_SECRET'],
                     username=redditapiconfig['USERNAME'],
                     password=redditapiconfig['PASSWORD'],
                     user_agent=redditapiconfig['USER_AGENT'])


class RedditApi:
    def __init__(self, q):
        if q == 'general':
            self.q = 'news'
        else:
            self.q = q
        self.name = get_name()                          # Getting name from config for consistency
        self.news = list()

    def getNews(self) -> list:
        try:
            subreddit = reddit.subreddit(self.q)
            responseObject = subreddit.hot()            # API call

            for submission in responseObject:
                self.news.append({
                    'headline': submission.title,
                    'link': submission.url,
                    'source': self.name
                })
            return self.news

        except APIException as e:
            raise Exception("RedditAPI Exception: {}.".format(str(e)))
        except Exception as e:
            raise Exception("Newzology Exception: {}.".format(str(e)))

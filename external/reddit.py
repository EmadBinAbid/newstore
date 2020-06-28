import praw
from praw.exceptions import APIException
from rest_framework.response import Response
from config.redditapiconfig import get_redditapi_config, get_name

from nstorelogger.logger import Logger
log = Logger()

redditapiconfig = get_redditapi_config()
reddit = praw.Reddit(client_id=redditapiconfig['CLIENT_ID'],
                     client_secret=redditapiconfig['CLIENT_SECRET'],
                     username=redditapiconfig['USERNAME'],
                     password=redditapiconfig['PASSWORD'],
                     user_agent=redditapiconfig['USER_AGENT'])


class RedditApi:
    """
    This class handles all the communication with Reddit third-party API. 
    In order for this class to function properly, it is expected that a
    valid CLIENT_ID, CLIENT_SECRET, and USERNAME will be set in 
    config.redditapiconfig.py. This class uses 'praw' Python wrapper to 
    hit the requests.
    """

    def __init__(self, q):
        if q == 'general':
            self.q = 'news'
        else:
            self.q = q
        self.name = get_name()                          # Getting name from config for consistency
        self.news = list()

    def getNews(self) -> list:
        """
        Hits the Reddit API's endpoint using 'hot' wrapper function to 
        fetch all the news from API.

        Parameters:
        None

        Returns: 
        list: a list of dictionary objects containing news from Reddit API
        
        """
        try:
            subreddit = reddit.subreddit(self.q)
            responseObject = subreddit.hot()            # API call

            for submission in responseObject:
                self.news.append({
                    'headline': submission.title,
                    'link': submission.url,
                    'source': self.name
                })
            
            log.debug('Fetched data from Reddit API')
            return self.news

        except APIException as e:
            log.error('RedditAPI Exception:' + str(e))
            raise Exception("RedditAPI Exception: {}.".format(str(e)))
        except Exception as e:
            log.error('Newstore Exception:' + str(e))
            raise Exception("Newstore Exception: {}.".format(str(e)))

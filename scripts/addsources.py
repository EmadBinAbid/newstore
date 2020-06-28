# Initial script that runs to add news sources from DB

from config.redditapiconfig import get_name as reddit_name
from config.newsapiconfig import get_name as newsapi_name
from api.serializers import SourcesSerializer
from api.models import Sources
from scripts.fetchsources import fetch_sources

from nstorelogger.logger import Logger
log = Logger()

def add_sources() -> None:
    try:
        # Reddit
        sourcesList = Sources.objects.filter(source=reddit_name()).values('id')     # DB call
        if (len(sourcesList) == 0):
            sourcesSerializer = SourcesSerializer(data={'source': reddit_name()})

            if sourcesSerializer.is_valid():
                sourcesSerializer.save()                                            # DB call
                log.debug('Added new news source to DB -> ' + reddit_name())
        else:
            log.debug('News source already ' + reddit_name() +  ' present in DB')

        # NewsAPI
        sourcesList = Sources.objects.filter(source=newsapi_name()).values('id')    # DB call
        if (len(sourcesList) == 0):
            sourcesSerializer = SourcesSerializer(data={'source': newsapi_name()})

            if sourcesSerializer.is_valid():
                sourcesSerializer.save()                                            # DB call
                log.debug('Added new news source to DB -> ' + newsapi_name())
        else:
            log.debug('News source already ' + newsapi_name() +  ' present in DB')
    except Exception as e:
        log.error('Newstore Exception: ' + 'Could not add news sources to DB: ' + str(e))

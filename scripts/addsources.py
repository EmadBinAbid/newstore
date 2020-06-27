# Initial script that runs to add news sources from DB

from config.redditapiconfig import get_name as reddit_name
from config.newsapiconfig import get_name as newsapi_name

from api.serializers import SourcesSerializer
from api.models import Sources

from scripts.fetchsources import fetch_sources

def add_sources() -> None:
    # Reddit
    sourcesList = Sources.objects.filter(source=reddit_name()).values('id')
    if (len(sourcesList) == 0):
        sourcesSerializer = SourcesSerializer(data={'source': reddit_name()})

        if sourcesSerializer.is_valid():
            sourcesSerializer.save()
            fetch_sources()
    else:
        # add message to logs
        pass

    # NewsAPI
    sourcesList = Sources.objects.filter(source=newsapi_name()).values('id')
    if (len(sourcesList) == 0):
        sourcesSerializer = SourcesSerializer(data={'source': newsapi_name()})

        if sourcesSerializer.is_valid():
            sourcesSerializer.save()
    else:
        # add message to logs
        pass

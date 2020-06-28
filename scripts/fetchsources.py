# Initial script that runs to add news sources from DB

from config.redditapiconfig import get_name as reddit_name
from config.newsapiconfig import get_name as newsapi_name
from api.serializers import SourcesSerializer
from api.models import Sources
from universal.universal import Universal

from nstorelogger.logger import Logger
log = Logger()

def fetch_sources() -> None:
    try:
        sourcesList = Sources.objects.all()                         # DB call
        serializer = SourcesSerializer(sourcesList, many=True)

        # Storing data in a static dict from Universal module
        sourcesDict = dict()
        for data in serializer.data:
            sourcesDict[data['source']] = data['id']

        Universal.setNewsSources(sourcesDict)
        log.debug('Fetched news sources from DB and stored in static instance')
    except Exception as e:
        log.error('Newstore Exception: ' + 'Could not fetch news sources from DB: ' + str(e))

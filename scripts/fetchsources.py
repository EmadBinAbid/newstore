# Initial script that runs to add news sources from DB

from config.redditapiconfig import get_name as reddit_name
from config.newsapiconfig import get_name as newsapi_name

from api.serializers import SourcesSerializer
from api.models import Sources

from universal.universal import Universal

def fetch_sources() -> None:
    # Reddit
    sourcesList = Sources.objects.all()
    serializer = SourcesSerializer(sourcesList, many=True)

    sourcesDict = dict()
    # cache the data here
    for data in serializer.data:
        sourcesDict[data['source']] = data['id']

    Universal.setNewsSources(sourcesDict)
    print(Universal.getNewsSources())

    print("SOURCES LIST")
    print(serializer.data)
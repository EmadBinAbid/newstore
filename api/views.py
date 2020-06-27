from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import News, Keywords, NewsHistory, Sources
from .serializers import NewsSerializer, KeywordsSerializer, SourcesSerializer
from external import newstorehandler as nh
from config.appconfig import get_data_expiry_timedelta, is_news_history_table_active
from universal.universal import Universal

import datetime as dt

from nstorelogger.logger import Logger
log = Logger()

# Create your views here.

@api_view(['GET'])
def news_list(request) -> Response:
    try:
        searchCategory = 'general'
        if request.query_params.get('query') != None:
            searchCategory = request.query_params.get('query')

        keywordId = getKeywordId(searchCategory)

        # Check if news has expired
        newsList = News.objects.filter(keyword_id_id=keywordId, expiry_date__gt=dt.datetime.now())

        if (len(newsList) == 0):
            # Delete previous records against this keyword
            News.objects.filter(keyword_id_id=keywordId).delete()

            # Make a fresh API call to all third party APIs
            newsList = nh.NewstoreHandler(searchCategory).getAllNews()
            nextTime = dt.datetime.now() + dt.timedelta(minutes=get_data_expiry_timedelta()['MINUTES'])
            newsSources = Universal.getNewsSources()

            # Add data to newshistory table if flag set to True
            if is_news_history_table_active():
                newsObjectsHistoryTable = (NewsHistory(headline=news['headline'], link=news['link'],
                                source_id_id=newsSources[news['source']], keyword_id_id=keywordId, expiry_date=nextTime) for news in newsList)
                createdNewsList = NewsHistory.objects.bulk_create(newsObjectsHistoryTable)

            # Add data to actual News table
            newsObjects = (News(headline=news['headline'], link=news['link'],
                                source_id_id=newsSources[news['source']], keyword_id_id=keywordId, expiry_date=nextTime) for news in newsList)
            createdNewsList = News.objects.bulk_create(newsObjects)
            serializer = NewsSerializer(createdNewsList, many=True)
            return Response(serializer.data)
        else:
            # Return same data from the DB
            serializer = NewsSerializer(newsList, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response({'message': str(e)})

@api_view(['GET'])
def sources_list(request) -> Response:
    try:
        sourcesList = Sources.objects.all()
        serializer = SourcesSerializer(sourcesList, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'message': str(e)})

def getKeywordId(keyword) -> int:
    keywordId = None

    # Check if keyword already exists
    keywordsList = Keywords.objects.filter(keyword=keyword).values('id')
    if (len(keywordsList) == 0):
        # Add keyword to DB if not already present
        keywordsSerializer = KeywordsSerializer(data={'keyword': keyword})
        if keywordsSerializer.is_valid():
            keywordsSerializer.save()
        keywordId = Keywords.objects.filter(keyword=keyword).values('id')[0]['id']
    else:
        # Return keyword id if present
        keywordId = keywordsList[0]['id']
    return keywordId
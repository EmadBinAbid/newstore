from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import News, Keywords, NewsHistory
from .serializers import NewsSerializer, KeywordsSerializer
from external import newstorehandler as nh
from config.appconfig import get_data_expiry_timedelta, is_news_history_table_active

import datetime as dt

from nstorelogger.logger import Logger
log = Logger()

# Create your views here.

@api_view(['GET'])
def news_list(request):
    log.debug('Hi this is emadddddd')
    log.error('Emad :((((')
    try:
        searchCategory = 'general'
        if request.query_params.get('query') != None:
            searchCategory = request.query_params.get('query')

        # search for keyword in db
        keywordsList = Keywords.objects.filter(
            keyword=searchCategory).values('id')
        keywordId = None
        if (len(keywordsList) == 0):
            keywordsSerializer = KeywordsSerializer(
                data={'keyword': searchCategory})
            if keywordsSerializer.is_valid():
                keywordsSerializer.save()

            keywordId = Keywords.objects.filter(
                keyword=searchCategory).values('id')[0]['id']
        else:
            keywordId = keywordsList[0]['id']

        print(keywordId)

        # if keyword not found, insert this keyword else fetch results from db against this keyword
        newsList = News.objects.filter(
            keyword_id_id=keywordId, expiry_date__gt=dt.datetime.now())
        print(newsList)

        if (len(newsList) == 0):
            # return database response
            print('from api')
            newsList = nh.NewstoreHandler(searchCategory).getAllNews()

            nextTime = dt.datetime.now() + dt.timedelta(minutes=get_data_expiry_timedelta()['MINUTES'])

            if is_news_history_table_active():
                newsObjectsHistoryTable = (NewsHistory(headline=news['headline'], link=news['link'],
                                source=news['source'], keyword_id_id=keywordId, expiry_date=nextTime) for news in newsList)
                # bulk_create has its own demerits
                createdNewsList = NewsHistory.objects.bulk_create(newsObjectsHistoryTable)
                


            newsObjects = (News(headline=news['headline'], link=news['link'],
                                source=news['source'], keyword_id_id=keywordId, expiry_date=nextTime) for news in newsList)

            # bulk_create has its own demerits
            createdNewsList = News.objects.bulk_create(newsObjects)
            serializer = NewsSerializer(createdNewsList, many=True)
            return Response(serializer.data)
        else:
            # make an api call
            print('from db')
            serializer = NewsSerializer(newsList, many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response({'message': str(e)})

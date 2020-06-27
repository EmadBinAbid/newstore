from rest_framework import serializers
from .models import News, Keywords, NewsHistory

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('headline', 'link', 'source')

class NewsHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsHistory
        fields = ('headline', 'link', 'source')

class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keywords
        fields = ('keyword', 'created_at')

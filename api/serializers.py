from rest_framework import serializers
from .models import News, Keywords, NewsHistory, Sources

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('headline', 'link', 'source_id_id')

class NewsHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsHistory
        fields = ('headline', 'link', 'source_id_id')

class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keywords
        fields = ('keyword', 'created_at')

class SourcesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sources
        fields = ('id', 'source')

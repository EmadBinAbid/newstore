from rest_framework import serializers
from .models import News, Keywords

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('headline', 'link', 'source')

class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keywords
        fields = ('keyword', 'created_at')

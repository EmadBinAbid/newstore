from django.contrib import admin
from .models import News, Keywords, NewsHistory

# Register your models here.

admin.site.register(News)
admin.site.register(NewsHistory)
admin.site.register(Keywords)
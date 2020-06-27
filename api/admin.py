from django.contrib import admin
from .models import News, Keywords, NewsHistory, Sources

from scripts.addsources import add_sources          # Adds news sources in DB
from scripts.fetchsources import fetch_sources      # Fetches existing sources from DB

# Register your models here.

admin.site.register(News)
admin.site.register(NewsHistory)
admin.site.register(Keywords)
admin.site.register(Sources)

# Initial script that runs to add news sources from DB
add_sources()

# Initial script that runs to fetch news sources from DB and stores in in-memory cache
fetch_sources()

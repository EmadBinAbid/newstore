from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('news/', views.news_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
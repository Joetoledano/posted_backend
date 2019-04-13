from django.urls import include, path
from rest_framework import routers
from posted.api import views
from django.urls import path, re_path, include


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^users/$', views.userview),
    re_path(r'^deals/$', views.deals),
    re_path(r'^groups/$', views.groupview),
    re_path(r'^check/$', views.check),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

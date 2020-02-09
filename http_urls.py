from django.urls import include, path
from rest_framework import routers

from apps.views.apps import AppViewSet

app_name = 'apps'

router = routers.SimpleRouter()
router.register(r'app', AppViewSet, basename='app')

urlpatterns = [
    path('', include(router.urls)),
]

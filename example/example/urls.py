from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from .views import Cluster


router = DefaultRouter()
router.register('cluster', Cluster)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

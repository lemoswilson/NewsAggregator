from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('news', views.FactMag_news)

router2 = routers.DefaultRouter()
router2.register('tech', views.FactMag_tech)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
]
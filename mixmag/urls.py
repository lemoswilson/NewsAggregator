from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("news", views.MixMag_news)

router2 = routers.SimpleRouter()
router2.register('tech', views.MixMag_tech)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls)),
]
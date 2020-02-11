from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("news", views.MixMag_news)

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register("news", views.ResidentAdvisor_news)

urlpatterns = [
    path("", include(router.urls)),
]
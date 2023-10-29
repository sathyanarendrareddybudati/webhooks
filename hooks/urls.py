from django.contrib import admin
from django.urls import path
from .views import Webhook

urlpatterns = [
    path('api/<int:version>/webhook/', Webhook.as_view()),
]

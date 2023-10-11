from django.urls import path

from . import views


# polls url configs
urlpatterns = [path("", views.index, name="index")]

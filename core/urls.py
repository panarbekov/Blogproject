from django.urls import path
from .views import *

urlpatterns = [
    path("all/", articles, name="articles"),
    path("<id>/", article, name="article"),
    path("<id>/", add, name = "add"),
    path("<id>/edit/", edit, name= "edit"),
]
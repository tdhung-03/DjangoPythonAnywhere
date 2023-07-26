from django.urls import path
from .views import *

urlpatterns = [
    path("", list, name="list"),
    path("post/<str:pk>", post, name="post"),
]

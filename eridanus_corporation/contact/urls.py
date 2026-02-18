from django.contrib import admin
from django.urls import path
from .views import BlogCreateView

urlpatterns = [
    path('',BlogCreateView.as_view(),name="contact")
]

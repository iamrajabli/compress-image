from django.urls import path
from . import views

urlpatterns = [
    path('', views.compress_and_download, name='compress_and_download'),
]

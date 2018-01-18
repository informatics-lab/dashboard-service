from django.urls import path

from . import views

urlpatterns = [
    path('', views.simple_chart, name='simple_chart'),
]


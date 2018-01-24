from django.urls import path

from . import views

urlpatterns = [
    path('<int:dashboard_id>', views.dashboard, name='dashboard'),
]


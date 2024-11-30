# service_requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('admin/manage/', views.admin_manage_requests, name='admin_manage_requests'),
]

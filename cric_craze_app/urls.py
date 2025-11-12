from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/v1/live-streams/", views.live_streams, name="live_streams"),
    path("api/v1/crousel-data/", views.crousel_data, name="crousel_data"),
    path('latest-app-version/', views.LatestAppVersionView.as_view(), name='latest-app-version'),
]


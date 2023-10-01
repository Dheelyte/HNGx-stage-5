from .views import VideoHandler
from django.urls import path


urlpatterns = [
    path('video/', VideoHandler.as_view())
]

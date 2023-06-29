from django.urls import path

from .views import CurrentDateView, IndexView


urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('', IndexView.as_view()),
]

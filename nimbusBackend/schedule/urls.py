from django.urls import path
from .views import ScheduleView, ScheduleListView

urlpatterns = [
    path("", ScheduleListView.as_view()),
    path("<str:pk>", ScheduleView.as_view()),
]
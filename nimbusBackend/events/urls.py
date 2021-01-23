from django.urls import path

from events.views import EventsView, EventView

urlpatterns = [
    path("", EventsView.as_view()),
    path("<str:pk>", EventView.as_view()),

]
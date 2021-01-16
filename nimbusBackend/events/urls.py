from django.urls import path

from events.views import EventsView, DepartmentalEventsView, DepartmentalEventView ,\
    InstitutionalEventsView, InstitutionalEventView, TalksView, TalkView, \
        ExhibitionsView, ExhibitionView, WorkshopsView, WorkshopView

urlpatterns = [
    path("", EventsView.as_view()),
    
    path("departmental/", DepartmentalEventsView.as_view()),
    path("departmental/<str:pk>", DepartmentalEventView.as_view()),

    
    path("institutional/", InstitutionalEventsView.as_view()),
    path("institutional/<str:pk>", InstitutionalEventView.as_view()),

    path("talk/", TalksView.as_view()),
    path("talk/<str:pk>", TalkView.as_view()),

    path("exhibition/", ExhibitionsView.as_view()),
    path("exhibition/<str:pk>", ExhibitionView.as_view()),

    path("workshop/", WorkshopsView.as_view()),
    path("workshop/<str:pk>", WorkshopView.as_view()),

]
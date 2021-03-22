from django.urls import path

from . import views
# from users.views import UserView, UsersView

urlpatterns = [
    path("joinvc/<str:uid>", views.joinVCView),
    path("log/<str:channel>", views.logView),
    path("report/<str:uid>", views.reportView),
    path("report/", views.reportNewView),
]
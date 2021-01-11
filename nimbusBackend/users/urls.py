from django.urls import path

from users.views import UserView, UsersView

urlpatterns = [
	path("", UsersView.as_view()),
    path("<str:pk>/", UserView.as_view()),
]
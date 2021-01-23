from django.urls import path

from . import views
# from users.views import UserView, UsersView

urlpatterns = [
	# path("", UsersView.as_view()),
    # path("<str:pk>/", UserView.as_view()),
    path("joinvc/<str:uid>", views.joinVCView)
]
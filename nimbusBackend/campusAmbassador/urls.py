from django.urls import path
from .views import CampusAmbassadorPostView, CampusAmbassadorPostsView, IsCampusAmbassador

urlpatterns = [
    path("post", CampusAmbassadorPostsView.as_view()),
    path("post/<str:pk>", CampusAmbassadorPostView.as_view()),
    path("isCampusAmbassador/<str:pk>", IsCampusAmbassador.as_view()),
]
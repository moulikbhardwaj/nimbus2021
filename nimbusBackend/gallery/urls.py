from gallery.models import GalleryPost
from django.urls import path

from gallery.views import GalleryListView, GalleryDestroyView

urlpatterns = [
    path('', GalleryListView.as_view()),
    path('<str:pk>/', GalleryDestroyView.as_view()),
]
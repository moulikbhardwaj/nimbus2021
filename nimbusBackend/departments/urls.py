from django.urls import path

from departments.views import DepartmentView, DepartmentsView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path("", DepartmentsView.as_view()),
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("<str:pk>", DepartmentView.as_view()),
]
from django.urls import path

from departments.views import DepartmentView, DepartmentsView

urlpatterns = [
	path("", DepartmentsView.as_view()),
    path("<str:pk>", DepartmentView.as_view()),
]
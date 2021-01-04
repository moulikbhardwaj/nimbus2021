from django.urls import path

from backend.views import DepartmentsView, DepartmentView, QuestionView, QuestionsView, QuizView, QuizzesView, UsersView, UserView

urlpatterns = [
    # User related URLS
    path("users/", UsersView.as_view()),
    path("users/<str:pk>", UserView.as_view()),

    # Department related URLS
    path("departments/", DepartmentsView.as_view()),
    path("department/<str:pk>", DepartmentView.as_view()),

    # Quiz related URLS
    path("quizzes/", QuizzesView.as_view()),
    path("quiz/<str:pk>", QuizView.as_view()),
    
    path("questions/", QuestionsView.as_view()),
    path("question/<str:pk>", QuestionView.as_view()),

]
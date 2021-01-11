from django.urls import path

from quiz.views import QuizView, QuizzesView

urlpatterns = [
	path("", QuizzesView.as_view()),
    path("<str:pk>", QuizView.as_view()),
    
]
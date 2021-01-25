from django.urls import path

from .views import LoginView, CreateQuestionView, CreateQuizView, LogoutView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="quizPanelHome"),
    path('login/', LoginView.as_view(), name="quizPanelLogin"),
    path('logout/', LogoutView.as_view(), name="quizPanelLogout"),
    path('create-question/', CreateQuestionView.as_view(), name="quizPanelCreateQuestion"),
    path('create-quiz/', CreateQuizView.as_view(), name="quizPanelCreateQuiz")
]

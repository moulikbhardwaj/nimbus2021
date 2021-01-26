from django.urls import path

from .views import LoginView, CreateQuestionView, CreateQuizView, LogoutView, HomeView, QuizView, UpdateQuestionView, \
    UpdateQuizView

urlpatterns = [
    path('', HomeView.as_view(), name="quizPanelHome"),
    path('login/', LoginView.as_view(), name="quizPanelLogin"),
    path('logout/', LogoutView.as_view(), name="quizPanelLogout"),
    path('create-question/<str:id>/', CreateQuestionView.as_view(), name="quizPanelCreateQuestion"),
    path('update-question/<str:id>/', UpdateQuestionView.as_view(), name="quizPanelUpdateQuestion"),
    path('update-quiz/<str:id>/', UpdateQuizView.as_view(), name="quizPanelUpdateQuiz"),
    path('create-quiz/', CreateQuizView.as_view(), name="quizPanelCreateQuiz"),
    path('quizDetails/<str:id>/', QuizView.as_view(), name="quizPanelQuizDetails")
]

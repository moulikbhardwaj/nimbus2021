from django.urls import path

from quiz.views import QuizView, QuizzesView, LeaderBoard, QuizLeaderBoard, QuestionView

urlpatterns = [
    path("", QuizzesView.as_view()),
    path("<str:pk>", QuizView.as_view()),
    path("leaderboard/results/", LeaderBoard.as_view()),
    path("leaderboard/results/<str:pk>/", QuizLeaderBoard.as_view()),
    path("question/<str:pk>/", QuestionView.as_view())
]

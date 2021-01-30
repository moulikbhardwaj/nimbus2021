from django.urls import path

from .views import LoginView, CreateQuestionView, CreateQuizView, LogoutView, HomeView, QuizView, UpdateQuestionView, \
    UpdateQuizView, ChooseQuizView, LeaderBoardView, export_leaderboard_xls, UploadQuestionUsingExcelSheetView, DeleteQuizQuestionView

urlpatterns = [
    path('', HomeView.as_view(), name="quizPanelHome"),
    path('login/', LoginView.as_view(), name="quizPanelLogin"),
    path('logout/', LogoutView.as_view(), name="quizPanelLogout"),
    path('create-question/<str:id>/', CreateQuestionView.as_view(), name="quizPanelCreateQuestion"),
    path('update-question/<str:id>/', UpdateQuestionView.as_view(), name="quizPanelUpdateQuestion"),
    path('update-quiz/<str:id>/', UpdateQuizView.as_view(), name="quizPanelUpdateQuiz"),
    path('create-quiz/', CreateQuizView.as_view(), name="quizPanelCreateQuiz"),
    path('select-quiz/', ChooseQuizView.as_view(), name="quizPanelChooseQuiz"),
    path('quizDetails/<str:id>/', QuizView.as_view(), name="quizPanelQuizDetails"),
    path('quizLeaderBoard/<str:id>', LeaderBoardView.as_view(), name="quizPanelQuizLeaderboard"),
    path('quizLeaderBoard/GenerateExcel/<str:id>', export_leaderboard_xls, name="quizPanelLeaderBoardGenerateExcel"),
    path('uploadQuestion/<str:id>/', UploadQuestionUsingExcelSheetView.as_view(),
         name="quizPanelQuestionsUsingExcelSheet"),
    path('deleteQuestion/<str:id>', DeleteQuizQuestionView.as_view(), name="quizPanelDeleteQuestion")

]

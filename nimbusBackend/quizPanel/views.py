from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, CreateQuestionForm, QuizForm
from quiz.models import Quiz


class LoginView(View):

    def get(self, request):
        return render(request, template_name="auth/login.html", context={"form": LoginForm(), "title": "Login"})

    def post(self, request):
        pass


class LogoutView(View):

    def get(self, request):
        return render(request, template_name="auth/logout.html", context={"title": "Logout"})

    def post(self, request):
        pass


class CreateQuestionView(View):

    def get(self, request):
        return render(request, template_name="quiz/create-question.html",
                      context={"form": CreateQuestionForm(), "title": "Create Question"})

    def post(self, request):
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("success")
            return HttpResponseRedirect(reverse_lazy("quizPanelLogin"))
        else:
            return render(request, template_name="quiz/create-question.html",
                          context={"form": CreateQuestionForm(), "title": "Create Question"})


class CreateQuizView(View):
    def get(self, request):
        return render(request, template_name="quiz/create-quiz.html",
                      context={"form": QuizForm(), "title": "Create Quiz"})


class HomeView(View):

    def get(self, request):
        quizzes = Quiz.objects.all()
        return render(request, template_name="quiz/Home.html", context={"title": "Home", "quizzes": quizzes})

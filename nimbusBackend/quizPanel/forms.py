from django import forms
from django.forms import CharField, IntegerField, ChoiceField
from departments.models import Department
from quiz.models import Quiz


class LoginForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "password"]


class CreateQuestionForm(forms.Form):
    question_statement = CharField(max_length=256, min_length=5, widget=forms.Textarea)
    option_1 = CharField(max_length=256, min_length=1)
    option_2 = CharField(max_length=256, min_length=1)
    option_3 = CharField(max_length=256, min_length=1)
    option_4 = CharField(max_length=256, min_length=1)
    correct_option = ChoiceField(choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')))


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["name", "startTime", "endTime", "count", "sendCount"]
        widgets = {
            'startTime': DateInput(attrs={'type': 'datetime-local'}),
            'endTime': DateInput(attrs={'type': 'datetime-local'})
        }

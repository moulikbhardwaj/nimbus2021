from django import forms
from django.forms import CharField, IntegerField, ChoiceField, URLField
from departments.models import Department
from quiz.models import Quiz
from bootstrap_datepicker_plus import DateTimePickerInput


class LoginForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "password"]


class CreateQuestionForm(forms.Form):
    question_statement = CharField(max_length=256, min_length=5, widget=forms.Textarea)
    image = URLField(required=False, help_text="URL of image to be used in question (If any)")
    optionCount = IntegerField(initial=4, max_value=4, min_value = 2,
                                help_text="Number of options in quiz. if set to a lower number, leftover options will be ignored")

    option_1 = CharField(max_length=256, min_length=1, required=False)
    image_1 = URLField(required=False, help_text="URL of image to be used in question (If any)")

    option_2 = CharField(max_length=256, min_length=1, required=False)
    image_2 = URLField(required=False, help_text="URL of image to be used in question (If any)")

    option_3 = CharField(max_length=256, min_length=1, required=False)
    image_3 = URLField(required=False, help_text="URL of image to be used in question (If any)")

    option_4 = CharField(max_length=256, min_length=1, required=False)
    image_4 = URLField(required=False, help_text="URL of image to be used in question (If any)")

    correct_option = ChoiceField(help_text="Choose a correct option from dropdown menu",
                                 choices=((1, '1'), (2, '2'), (3, '3'), (4, '4')))


    timeLimit = IntegerField(initial=15, help_text="Time limit for the question (in seconds)")


    def clean(self):
        cleanded_data = super().clean()
        correct_option = cleanded_data['correct_option']
        option_count = cleanded_data['optionCount']
        if option_count<int(correct_option):
            raise forms.ValidationError({"correct_option":"Correct Option number is greater than option count"})

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ["name", "startTime", "endTime", "sendCount"]
        widgets = {
            'startTime': DateTimePickerInput(),
            'endTime': DateTimePickerInput()
        }

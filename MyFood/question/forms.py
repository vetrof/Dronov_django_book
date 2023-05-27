from django.forms import ModelForm

from question.models import QuestionModel


class QuestionModelForm(ModelForm):
    class Meta:
        model = QuestionModel
        fields = ('name', 'email', 'question')

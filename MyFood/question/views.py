from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from foodlist.models import Type, Food
from question.forms import QuestionModelForm
from question.models import QuestionModel


# class QuestionFormView(CreateView):
#     template_name = 'question/question.html'
#     form_class = QuestionModelForm
#     success_url = reverse_lazy('index')


class QuestionFormView(CreateView):
    template_name = 'question/question.html'
    model = QuestionModel
    fields = ('name', 'email', 'question')
    success_url = reverse_lazy('index')




class CrispyCreateView(CreateView):
    model = QuestionModel
    template_name = 'question/crispy.html'
    fields = ['name', 'email', 'question']
    success_url = reverse_lazy('index')


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     foods = Food.objects.all()
    #     types = Type.objects.all()
    #     context['foods'] = foods
    #     context['types'] = types
    #     return context


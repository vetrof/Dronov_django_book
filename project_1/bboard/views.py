from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bboard.models import Bd, Rubric


def index_view(request):
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def index_rubric_view(request, by_rubric):
    bbs = Bd.objects.filter(rubric=by_rubric)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=by_rubric)

    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/index.html', context)

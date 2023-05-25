from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from bboard.models import Bd


def index_view(request):
    bbs = Bd.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

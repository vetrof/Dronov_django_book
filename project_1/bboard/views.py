from django.shortcuts import render
from django.http import HttpResponse

from bboard.models import Bd


def index_view(request):
    s = 'список обьявлений\r\n\r\n\r\n'
    for bd in Bd.objects.order_by('-published'):
        s += f'{bd.title} : {bd.content} : {bd.price} \r\n\r\n'

    return HttpResponse(s, content_type='text/plain; charset=utf-8')

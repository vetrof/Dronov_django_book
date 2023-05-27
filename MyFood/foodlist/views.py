from django.shortcuts import render

from foodlist.models import Food, Type


def index_page(request):
    foods = Food.objects.all().order_by('-id')
    types = Type.objects.all()
    context = {'foods': foods, 'types': types}
    return render(request, 'fiidlist/index.html', context)


def index_page_type(request, type_id):
    foods = Food.objects.filter(type=type_id)
    types = Type.objects.all()
    current_type = Type.objects.get(pk=type_id)
    context = {'foods': foods, 'types': types, 'current_type': current_type}

    return render(request, 'fiidlist/index.html', context)

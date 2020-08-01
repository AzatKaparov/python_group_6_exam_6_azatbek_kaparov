from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Guestbook
from django.http import HttpResponseNotFound, HttpResponseNotAllowed

# В index добавлен фильтр


def index_view(request):
    all = Guestbook.objects.all().order_by('-created_date')
    data = []
    for i in all:
        if i.status =='active':
            data.append(i)
        else:
            pass
    return render(request, 'index.html', context={
        'guests': data
    })

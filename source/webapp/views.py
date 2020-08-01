from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Guestbook
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from .forms import CreateForm

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


def create_view(request, *args, **kwargs):
    if request.method == "GET":
        form = CreateForm()
        return render(request, 'create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = CreateForm(data=request.POST)
        if form.is_valid():
            task = Guestbook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
        else:
            return render(request, 'create.html', context={
                'form': form
            })

        return redirect('index')
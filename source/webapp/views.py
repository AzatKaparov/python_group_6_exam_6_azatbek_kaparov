from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Guestbook
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from .forms import CreateForm


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
            guest = Guestbook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
        else:
            return render(request, 'create.html', context={
                'form': form
            })

        return redirect('index')


def update_view(request, pk):
    guest = get_object_or_404(Guestbook, pk=pk)
    if request.method == "GET":
        form = CreateForm(initial={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
        })
        return render(request, 'update.html', context={
            'form': form,
            'guest': guest
        })
    elif request.method == 'POST':
        form = CreateForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data['name']
            guest.email = form.cleaned_data['email']
            guest.text = form.cleaned_data['text']
            guest.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={
                'guest': guest,
                'form': form,
                'errors': form.errors
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def delete_view(request, pk):
    guest = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
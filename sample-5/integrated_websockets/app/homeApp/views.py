from django.shortcuts import render, redirect
from .models import *
from .forms import HomeForm

def index(request):
    record = HomeModel.objects.last()
    print("Homepage record:", record)
    form = HomeForm()
    # print("record image:", record.image)
    context = {
        'record': record,
        'form': form,
    }
    return render(request, 'homeApp/index.html', context)

def uploadok(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("A new record is created!")
            return redirect('index')

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Person

class PersonPageView(View):
    def get(self, request):
        return render(request, 'personApp/index.html')
    
    def post(self, request):
        Person.objects.create(name=request.POST.get("name"))
        return render(request, 'personApp/index.html')
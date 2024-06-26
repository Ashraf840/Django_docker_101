from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Person

class PersonPageView(View):
    def get(self, request):
        persons = Person.objects.all()
        context = {'persons':persons}
        return render(request, 'personApp/index.html', context)
    
    def post(self, request):
        # print("Image:", request.FILES.get('image'))
        image = request.FILES.get('image')
        Person.objects.create(
            name=request.POST.get("name"),
            profile_pic=image if image else None
        )
        return redirect('personApp:PersonPageView')
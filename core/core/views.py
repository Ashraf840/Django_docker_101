from django.shortcuts import render

# create the templates folder imside the core application of this Dj proj

def home(request):
    return render(request, 'index.html')

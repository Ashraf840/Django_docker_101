from django.shortcuts import render
from django.views.generic import View


class samplePageView(View):
    template_name = 'sampleApp/index.html'

    def get(self, request):
        return render(request, self.template_name)


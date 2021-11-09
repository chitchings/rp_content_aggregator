from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Episode

class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Episode

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['episodes'] = Episode.objects.filter().order_by('-pub_date')
        return context

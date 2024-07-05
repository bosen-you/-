from django.shortcuts import render
from django.views.generic import ListView , CreateView
from .models import Journal
from django.urls import reverse_lazy
# Create your views here.
class JournalList(ListView):
    model = Journal
    ordering = ['-id']

class JournalCreate(CreateView):
    model = Journal
    fields = ['content']
    success_url = reverse_lazy('jou_list')
    template_name = 'form.html'
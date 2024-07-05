from django.shortcuts import render
from django.views.generic import ListView
from .models import Journal
# Create your views here.
class JournalList(ListView):
    model = Journal
    ordering = ['-id']
    
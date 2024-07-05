from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView
from .models import Journal
from django.urls import reverse_lazy
# Create your views here.
#日誌列表
class JournalList(ListView):
    model = Journal
    ordering = ['-id']

#日誌新增
class JournalCreate(CreateView):
    model = Journal
    fields = ['content']
    success_url = reverse_lazy('jou_list')
    template_name = 'form.html'

#日誌修改
class JournalEdit(UpdateView):
    model = Journal
    fields = ['content']
    success_url = reverse_lazy('jou_list')
    template_name = 'form.html'
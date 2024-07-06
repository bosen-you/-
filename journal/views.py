from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from .models import Journal
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#日誌列表
class JournalList(LoginRequiredMixin , ListView):
    model = Journal
    ordering = ['-id']
    paginate_by = 3    #設定每頁最多顯示資料筆數

#日誌新增
class JournalCreate(LoginRequiredMixin , CreateView):
    model = Journal
    fields = ['content']
    success_url = reverse_lazy('jou_list')
    template_name = 'form.html'

#日誌修改
class JournalEdit(LoginRequiredMixin , UpdateView):
    model = Journal
    fields = ['content']
    success_url = reverse_lazy('jou_list')
    template_name = 'form.html'

#日誌刪除
class JournalDelete(LoginRequiredMixin , DeleteView):
    model = Journal
    success_url = reverse_lazy('jou_list')
    template_name = 'confirm_delete.html'


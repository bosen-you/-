from django.views.generic import *
from .models import Expense
from django.urls import reverse_lazy

# Create your views here.
#日誌列表紀錄
class ExpenseList(ListView):
    model = Expense
    ordering = ['-id']
    paginate_by = 10

#新增支出紀錄
class ExpenseCreate(CreateView):
    model = Expense
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('exp_list')

#修改支出紀錄
class ExpenseUpdate(UpdateView):
    model = Expense
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('exp_list')

#刪除支出紀錄
class ExpenseDelete(DeleteView):
    model = Expense
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('exp_list')

    

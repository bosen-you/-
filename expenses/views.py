from django.views.generic import *
from .models import Expense

# Create your views here.
#日誌列表紀錄
class ExpenseList(ListView):
    model = Expense
    ordering = ['-id']
    paginate_by = 10
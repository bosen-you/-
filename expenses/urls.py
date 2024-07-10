from django.urls import path
from .views import *

urlpatterns = [
    path('' , ExpenseList.as_view() , name = 'exp_list'),
    path('create' , ExpenseCreate.as_view() , name = 'exp_create'),
    path('<int:pk>/update/' , ExpenseUpdate.as_view() , name = 'exp_update'),
    path('<int:pk>/delete/' , ExpenseDelete.as_view() , name = 'exp_delete'),
]

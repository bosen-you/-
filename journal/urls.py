from django.urls import path
from .views import *

urlpatterns = [
    path('' , JournalList.as_view() , name = 'jou_list'),
    path('create/' , JournalCreate.as_view() , name = 'jou_create'),
    path('<int:pk>/edit/' , JournalEdit.as_view() , name = 'jou_edit'),
    path('<int:pk>/delete/' , JournalDelete.as_view() , name = 'jou_delete'),
]

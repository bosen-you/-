from django.urls import path
from .views import *

urlpatterns = [
    path('' , JournalList.as_view() , name = 'jou_list')
]

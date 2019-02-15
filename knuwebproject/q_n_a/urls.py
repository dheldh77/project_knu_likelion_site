from django.urls import path
from . import views

urlpatterns = [
    path(' ',views.qna,name='qna'),
    path('new/',views.new,name='qna_new'),
    path('create/',views.create,name="qna_create"),
    path('int:qna_num>/',views.detail,name='qna_detail'),
]
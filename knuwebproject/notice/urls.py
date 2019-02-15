from django.urls import path
from . import views

urlpatterns = [
    path(' ',views.notice,name="notice"),
    path('new/',views.new,name="notice_new"),
    path('create/',views.create,name="notice_create"),
    path('<int:notice_num>/',views.detail,name="notice_detail"),
    path('more/',views.more,name="notice_more"),
]
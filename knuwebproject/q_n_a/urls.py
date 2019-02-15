from django.urls import path
from . import views
app_name = 'qna'
urlpatterns = [
    path(' ',views.qna,name='qna'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name="create"),
    path('<int:qna_num>/',views.detail,name='detail'),
]
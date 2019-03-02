from django.urls import path,include
from . import views

app_name = 'qna'
urlpatterns = [
    path('',views.qna,name='board'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name="create"),
    path('<int:qna_id>/',views.detail,name='detail'),
    path('<int:qna_id>/delete/', views.delete, name='delete'),
    path('<int:qna_id>/edit/',views.edit, name='edit'),
    path('<int:qna_id>/update/', views.update, name='update'),
    path('<int:ans_id>/ans', views.ans,name='ans'),
    path('newQNA/', views.newQNA, name="newQNA"),
    path('<int:qna_id>/editQNA/', views.editQNA, name="editQNA"),
    path('search/',views.search, name="search"),
]
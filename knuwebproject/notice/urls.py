from django.urls import path
from . import views
app_name = 'notice'
urlpatterns = [
    path(' ',views.notice,name="notice"),
    path('new/',views.new,name="new"),
    path('create/',views.create,name="create"),
    path('<int:notice_id>/',views.detail,name="detail"),
    # path('more/',views.more,name="notice_more"),
]
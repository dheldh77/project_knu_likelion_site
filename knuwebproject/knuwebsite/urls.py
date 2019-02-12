"""knuwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
import notice.views
import q_n_a.views
import game.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.views.home,name="home"),
    path('history/',home.views.history,name="history"),
    path('five/', home.views.five, name="five"),
    path('six/', home.views.six, name="six"),
    path('seven/', home.views.seven, name="seven"),
    path('schedule/', home.views.schedule, name='schedule'),
    path('about/', home.views.about, name='about'),
    path('notice/',notice.views.notice,name="notice"),
    path('notice/new/',notice.views.new,name="notice_new"),
    path('notice/create/',notice.views.create,name="notice_create"),
    path('notice/<int:notice_num>/',notice.views.detail,name="notice_detail"),
    path('notice/more',notice.views.more,name="notice_more"),
    path('qna/',q_n_a.views.qna,name='qna'),
    path('qna/new/',q_n_a.views.new,name='qna_new'),
    path('qna/create/',q_n_a.views.create,name="qna_create"),
    path('qna/<int:qna_num>',q_n_a.views.detail,name='qna_detail'),
    path('shuffle/', game.views.shuffle, name="shuffle"),
    path('accounts/',include('accounts.urls')),
]

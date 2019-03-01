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
import interview.views
import gallery.views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.views.home,name="home"),
    path('history/',home.views.history,name="history"),
    path('five/', home.views.five, name="five"),
    path('six/', home.views.six, name="six"),
    path('seven/', home.views.seven, name="seven"),
    path('schedule/', home.views.schedule, name='schedule'),
    path('about/', home.views.about, name='about'),
    path('notice/',include('notice.urls')),
    path('qna/',include('q_n_a.urls')),
    path('accounts/',include('accounts.urls')),
    path('shuffle/', game.views.shuffle, name="shuffle"),
    path('interview/',interview.views.board, name="interview"),
    path('gallery/',gallery.views.board,name='gallery'),
    path(r'^upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path(r'^browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
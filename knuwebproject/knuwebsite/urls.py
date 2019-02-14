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
    path('notice/',include('notice.urls')),
    path('q_n_a/',include('q_n_a.urls')),
    path('accounts/',include('accounts.urls')),
    path('shuffle/', game.views.shuffle, name="shuffle"),
    path('interview/',interview.views.board, name="interview")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from .models import Notice, Pic

# Register your models here.


class PicInline(admin.TabularInline):
    model = Pic

class NoticeAdmin(admin.ModelAdmin):
    inlines = [PicInline,]

admin.site.register(Notice, NoticeAdmin)
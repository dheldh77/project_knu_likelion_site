from django.contrib import admin
from .models import Interview, Pic

# Register your models here.
class PicInline(admin.TabularInline):
    model = Pic

class InterviewAdmin(admin.ModelAdmin):
    inlines = [PicInline,]

admin.site.register(Interview, InterviewAdmin)
from django.contrib import admin
from .models import Gallery, Pic

# Register your models here.
class PicInline(admin.TabularInline):
    model = Pic

class GalleryAdmin(admin.ModelAdmin):
    inlines = [PicInline,]

admin.site.register(Gallery, GalleryAdmin)
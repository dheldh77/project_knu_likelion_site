from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Interview(models.Model):
    title = models.CharField(max_length = 255)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

class Pic(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.CharField(max_length = 255, null=True, blank=True)
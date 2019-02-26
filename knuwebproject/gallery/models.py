from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Pic(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='usr',blank=True, null=True)
    description = models.CharField(max_length=250)
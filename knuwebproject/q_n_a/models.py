from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class QNA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    description = RichTextUploadingField(blank=True,null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
    
class Photo(models.Model):
    qna = models.ForeignKey(QNA, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.CharField(max_length=200)

class Answer(models.Model):
    qna = models.ForeignKey(QNA, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
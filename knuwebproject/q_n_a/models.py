from django.db import models

# Create your models here.
class QNA(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title
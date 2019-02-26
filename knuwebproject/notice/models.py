from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('id',)
    
class Pic(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='usr', blank=True, null=True)
    description = models.CharField(max_length=200)
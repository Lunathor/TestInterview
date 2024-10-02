from django.db import models

# Create your models here.


class WordCount(models.Model):
    word = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    
    
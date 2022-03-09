from django.db import models
from django.forms import CharField
from tinymce import HTMLField

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =60)
    caption = models.TextField() 
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

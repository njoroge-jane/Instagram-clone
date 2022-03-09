from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =60)
    caption = models.TextField() 
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

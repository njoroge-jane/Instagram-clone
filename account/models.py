from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username  

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete() 

    @classmethod
    def search_by_user(cls,search_term):
        person = cls.objects.filter(user__icontains=search_term)
        return person   


class Comments(models.Model):
    comment = models.TextField()

    def save_comment(self):
        self.save()   

    def delete_comment(self):
        self.save()   

class Likes(models.Model):
    likes=models.IntegerField()

    def save_likes(self):
        self.save()

    def delete_likes(self):
        self.save()           



class Image(models.Model):
    title = models.CharField(max_length =60)
    caption = models.TextField() 
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE) 
    comments = models.ForeignKey(Comments,on_delete=models.CASCADE,null=True)
    likes = models.ForeignKey(Likes,on_delete=models.CASCADE,null=True)

    def save_image(self):
        self.save()  

    def delete_image(self):
        self.save()                     

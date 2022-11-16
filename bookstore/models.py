from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class genreCategory(models.Model):
    
    
    genre=models.CharField(max_length=100)
    

    def __str__(self):
        return self.genre

class ebook(models.Model):
    title=models.CharField(max_length=100)
    Auther=models.CharField(max_length=100)
    genre=models.ForeignKey(genreCategory,on_delete=models.CASCADE,related_name="ebooks")
    review=models.IntegerField()
    favorite=models.ManyToManyField(User,blank=True,related_name="users")


    def __str__(self):
        return self.title

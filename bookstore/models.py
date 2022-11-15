from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class genreCategory(models.Model):
    
    genre_category=(
        ("Fantasy","Fantasy"),
        ("Literary","Literary"),
        ("Mystery","Mystery"),
        ("Non-Fiction","Non-Fiction"),
        ("Science Fiction","Science Fiction"),
        ("Thriller","Thriller")
    )
    genre=models.CharField(max_length=100,choices=genre_category)


class ebook(models.Model):
    title=models.CharField(max_length=100)
    Auther=models.CharField(max_length=100)
    genre=models.ForeignKey(genreCategory,on_delete=models.CASCADE,related_name="genreCat")
    review=models.IntegerField()
    favorite=models.ManyToManyField(User,blank=True)


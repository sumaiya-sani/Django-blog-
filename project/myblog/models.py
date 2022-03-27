from asyncio.windows_events import NULL
from distutils.command.upload import upload
from random import choices
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from django.utils import timezone
from ckeditor.fields import RichTextField 
from django.db.models.signals import post_save


class Profile(models.Model):
    CENDER=(
        ('Male','Male'),
        ('Female','Female'),
    )
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_picture=models.ImageField(null=True,blank=True,upload_to="images/profile")
    cender=models.CharField(max_length=50,choices=CENDER,default='Male')
    website_url=models.CharField(max_length=255,blank=True,null=True)
    twitter_url=models.CharField(max_length=255,blank=True,null=True)
    facebook_url=models.CharField(max_length=255,blank=True,null=True)
    githube_url=models.CharField(max_length=255,blank=True,null=True)

    
    def create_profile(sender,**kwargs):
     if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)        


    def __str__(self):
        return str(self.user)

class Category_path(models.Model):
    
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myblog:home')      



class Post(models.Model):
    
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    header_photo=models.ImageField(blank=True,null=True,upload_to="images/")
    body=RichTextField(blank=True,null=True)
    date_of_post=models.DateField(auto_now_add=True) 
    category=models.ForeignKey(Category_path,on_delete=models.PROTECT,default=1)
    likes=models.ManyToManyField(User,related_name='like_post')
    snippets=models.CharField(max_length=255,default='continue reading')


    def __str__(self):
        return self.title +'|'+ str(self.author)
    def total_likes(self):
        return self.likes.count()    

    def get_absolute_url(self):
        return reverse('myblog:article_detail',args=(str(self.id)))  


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    data_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

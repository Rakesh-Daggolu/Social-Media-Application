from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as Luser
from django.core.files.storage import FileSystemStorage
import os
'''
user- uname,tag,desc,no of posts, no of followers,no of following,profile img,location,type of accounts(general/businness)

post- user,img,desc string,no of likes

collapsed comments
'''
fs = FileSystemStorage(location='/media/')
class User(models.Model):
    luser=models.ForeignKey(Luser,related_name='luser',on_delete=models.CASCADE)
    uname=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    nposts=models.IntegerField(default=0)
    nfollowers=models.IntegerField(default=0)
    nfollowing=models.IntegerField(default=0)
    pimg=models.ImageField(upload_to='images/',default='', blank=True)
    location=models.CharField(max_length=30)
    type=models.CharField(max_length=30,choices=[('general','General'),('bussiness','Bussiness')])

class Followers(models.Model):
    base_user=models.ForeignKey(User,related_name='base_user',on_delete=models.CASCADE,default=None)
    follower_user=models.ForeignKey(User,related_name='follower_user',on_delete=models.CASCADE)

class Post(models.Model):
    user=models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    liked=models.BooleanField(default=False)
    img=models.ImageField(upload_to='uploads/')
    body=models.CharField(max_length=50)
    nlikes=models.IntegerField()
    publish=models.DateTimeField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

class Likes(models.Model):
    user=models.ForeignKey(User,related_name='like',on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='like',on_delete=models.CASCADE)
class Comments(models.Model):
    comments=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

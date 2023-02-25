from django import forms
from django.contrib.auth.models import User as User1
from SocialApp.models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=User1
        fields=('username','password')

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('uname','description','location','pimg','type')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('img','body')

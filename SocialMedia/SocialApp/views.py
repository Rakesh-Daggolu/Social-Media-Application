from django.shortcuts import render
from SocialApp.models import *
from django.contrib.auth.decorators import login_required
from SocialApp.models import *
from django.contrib.auth.models import User as L_user
from django.shortcuts import get_object_or_404,redirect
from SocialApp.forms import *
from django.core.files.storage import FileSystemStorage
@login_required
def Home(request):
    uid=request.user.id
    print(uid)
    l=[]
    users=User.objects.all()
    for x in users.iterator():
        if x.luser.id!=uid:
            l.append(x)

    form=PostForm()
    if request.method=='POST':
        s=request.POST

        post=Post(user=User.objects.get(luser=request.user.id),img=request.FILES['img'],body=s['body'],nlikes=0)
        post.save()
    temp=User.objects.exclude(luser=request.user.id)
    #temp=temp.objects.filter(luser=Followers.objects.filter(follower_user=User.objects.get(luser=request.user.id).id))
    posts=Post.objects.filter(user__in=temp).order_by('modified_at')
    return render(request,'SocialApp/base.html',{'uid':uid,'users':l,'form':form,'posts':posts,'user':User.objects.get(luser=uid)})

def user_detail(request,id):
    user_=User.objects.get(luser=id)
    posts=user_.post.all().order_by('modified_at')

    if user_.nfollowers!=len(Followers.objects.filter(base_user=user_.id)):
        user_.nfollowers=len(Followers.objects.filter(base_user=user_.id))
        user_.save()
    elif user_.nfollowing!=len(Followers.objects.filter(follower_user=user_.id)):
        user_.nfollowers=len(Followers.objects.filter(follower_user=user_.id))
        user_.save()

    for post in posts.iterator():
        if post.nlikes!=post.like.all().count():
            post.nlikes=post.like.all().count()
            post.save()

    Logined_user=User.objects.get(luser=request.user.id)  #sham
    follower=False
    followings=Followers.objects.filter(follower_user=Logined_user.id) #people sham following(object 1- rakesh)

    for members in followings.iterator():
           if members.base_user.luser.id==id:    #rakesh matched - so unfollow option
               follower=True
               break

    return render(request,'SocialApp/user_detail.html',{'user':user_,'posts':posts,'logined_user':request.user.id,'follower':follower})

def post(request,id):
    post=Post.objects.get(id=id)
    if post.liked:
        Like=Likes.objects.get(user=User.objects.get(luser=request.user.id),post=post)
        Like.delete()
        post.nlikes-=1
        post.liked=False
    else:
        Like=Likes(user=User.objects.get(luser=request.user.id),post=post)
        Like.save()
        post.liked=True
        post.nlikes+=1

    post.save()
    return redirect("/profile/"+str(post.user.luser.id))

def followers(request,id):
    follower=Followers.objects.filter(base_user=id)
    return render(request,'SocialApp/followers.html',{'followers':follower})

def Signup(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            s=form.save(commit=True)
            s.set_password(s.password)
            s.save()
            return redirect('/user/'+str(s.id))
    return render(request,'SocialApp/signup.html',{'form':form})

def CreateUser(request,id):
    form=UserForm()
    print(id)
    if request.method=="POST":
        #s=UserForm(request.POST,request.FILES)
        s=request.POST
        User.objects.create(luser=L_user.objects.get(id=id),uname=s['uname'],description=s['description'],pimg=request.FILES['pimg'],location=s['location'],type=s['type'])
        return redirect('/profile/'+str(id))
    return render(request,'SocialApp/createprofile.html',{'form':form})

def Follows(request,id):
    id=int(id)
    Logined_user=User.objects.get(luser=request.user.id)   #rakesh-follower user,rakesh follows sham
    unfollow=False
    if id<0:
        unfollow=True
    id=abs(id)
    baseuser=User.objects.get(luser=id)     #sham - baseuser

    if unfollow:
        follows=Followers.objects.get(base_user=baseuser,follower_user=Logined_user)
        follows.delete()
    else:
        follows=Followers.objects.get_or_create(base_user=baseuser,follower_user=Logined_user)

    Logined_user.nfollowing=len(Followers.objects.filter(follower_user=Logined_user))
    baseuser.nfollowers=len(Followers.objects.filter(base_user=baseuser))
    Logined_user.save()
    baseuser.save()
    return user_detail(request,id)

def Upload(request,id):
    print(request.GET)
    user=User.objects.get(id=id)
    return redirect('/')

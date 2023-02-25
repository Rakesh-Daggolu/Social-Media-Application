from django.contrib import admin
from SocialApp.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=['uname']
    #fieldsets = [['some text',{'fields': ['uname','pimg']}],]

class PostAdmin(admin.ModelAdmin):
    list_display=['body']

class CommentAdmin(admin.ModelAdmin):
    list_display=['name']

class FollowerAdmin(admin.ModelAdmin):
    list_display=['follower_user']

class LikesAdmin(admin.ModelAdmin):
    list_display=['user']

class TestImage(admin.ModelAdmin):
    fieldsets = [['Some text', {'fields': ['img']}],]

admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Followers,FollowerAdmin)
admin.site.register(Likes,LikesAdmin)

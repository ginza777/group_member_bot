from django import forms
# Register your models here.
from django.contrib import admin
from botapp.models import Profile,Group_members,Group_members_api
# Register your models here.






@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('id','exeterenal_id','username','f_name','l_name','time')
@admin.register(Group_members)
class Group_membersAdmin(admin.ModelAdmin):
    list_display =('id','group_id','exeterenal_id','username','f_name','InvitedUserId','l_name','time','invited_status','is_bot','language_code')
    list_editable = ['invited_status']


@admin.register(Group_members_api)
class Group_members_apiAdmin(admin.ModelAdmin):
    list_display = ['id','group_id',
                    'exeterenal_id',
                    'username',
                    'f_name',
                    'l_name',
                    'phone',
                    'time',
                    'bot',
                    'lang_code',
                    'contact',
                    'premium'
                    ]

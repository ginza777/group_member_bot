from django.db import models
import datetime
# Create your models here.
from django.db import models
import datetime
# baza
class UserInvitedStatus(models.TextChoices):
    own = 'shaxsiy' ,  "Boshqa"
    byuser='byuser','User tomonidan'

class UserBotStatus(models.TextChoices):
      true='True','True'
      false='False','False'





class Profile(models.Model):
    exeterenal_id=models.PositiveIntegerField(
        verbose_name="user id",
        null=False
    )
    username=models.TextField(
        verbose_name="username",
        null=True,
        blank=True
    )
    f_name=models.TextField(
        verbose_name="First_name",
    )
    l_name=models.TextField(
        verbose_name="Lastname",
        null=True

    )
    time=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class Group_members(models.Model):
    group_id=models.CharField(max_length=125,null=True)
    exeterenal_id=models.PositiveIntegerField(
        verbose_name="user id",
        null=False
    )
    username=models.TextField(
        verbose_name="username",
        null=True,
        blank=True
    )
    f_name=models.TextField(
        verbose_name="First_name",
    )
    l_name=models.TextField(
        verbose_name="Lastname",
        null=True

    )
    time=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    invited_status=models.CharField(max_length=125,null=True, choices=UserInvitedStatus.choices)

    language_code=models.CharField(max_length=125,null=True,blank=True,default='uz')

    is_bot=models.CharField(default=False,max_length=20,choices=UserBotStatus.choices)

    InvitedUserId=models.PositiveIntegerField(null=True,blank=True,default=0)


class Group_members_api(models.Model):
    group_id=models.CharField(max_length=125,null=True,blank=True)
    exeterenal_id=models.PositiveIntegerField(null=False)
    username=models.TextField(null=True,blank=True)
    f_name=models.TextField(null=True,blank=True)
    l_name=models.TextField(null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    contact=models.CharField(max_length=125,null=True,blank=True)
    phone=models.CharField(max_length=125,null=True,blank=True)
    premium=models.CharField(max_length=125,null=True,blank=True)
    bot=models.CharField(max_length=125,null=True,blank=True)
    lang_code=models.CharField(max_length=125,null=True,blank=True)



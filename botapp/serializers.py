from rest_framework import serializers
from . import models


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['id', 'exeterenal_id', 'username', 'f_name','l_name', 'time']
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group_members
        fields = ['id', 'group_id', 'exeterenal_id','InvitedUserId', 'username', 'f_name','l_name', 'time', 'invited_status']

class Group_members_api_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group_members_api
        fields = [
                    'id',
                    'group_id',
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
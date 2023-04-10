from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, DestroyAPIView,RetrieveDestroyAPIView
from . import serializers
from . import models







class ProfilesSerializer(ListAPIView):
    serializer_class = serializers.ProfilesSerializer

    def get_queryset(self):
        return models.Profile.objects.all()

class ProfilesDestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.ProfilesSerializer

    def get_queryset(self):
        return models.Profile.objects.all()

class GroupSerializer(ListAPIView):
    serializer_class = serializers.GroupSerializer

    def get_queryset(self):
        return models.Group_members.objects.all()
class GroupDestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.GroupSerializer

    def get_queryset(self):
        return models.Group_members.objects.all()

class Group_members_api_Serializer(ListAPIView):
    serializer_class = serializers.Group_members_api_Serializer

    def get_queryset(self):
        return models.Group_members_api.objects.all()
class Group_members_api_DestroyApiView(RetrieveDestroyAPIView):
    serializer_class = serializers.Group_members_api_Serializer

    def get_queryset(self):
        return models.Group_members_api.objects.all()
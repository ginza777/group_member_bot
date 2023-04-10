from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('',HomePageView,name='home'),
    path('profiles/', views.ProfilesSerializer.as_view()),
    path('profiles/<int:pk>', views.ProfilesDestroyApiView.as_view()),
    path('groups/', views.GroupSerializer.as_view()),
    path('groups/<int:pk>', views.GroupDestroyApiView.as_view()),
    path('groups_api/', views.Group_members_api_Serializer.as_view()),
    path('groups_api/<int:pk>', views.Group_members_api_DestroyApiView.as_view()),

]

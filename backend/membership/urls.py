from django.urls import path,include
from .api import UserMembershipApi


urlpatterns = [
    path('user_membership',UserMembershipApi.as_view(),name="user_membership_create")
]
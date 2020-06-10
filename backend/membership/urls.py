from django.urls import path,include
from .api import MembershipPaymentApi,MembershipDetailApi,UserMembershipApi,MembershipApi,SubscriptionApi,SubscriptionDetailApi


urlpatterns = [
    path('user_membership/',UserMembershipApi.as_view(),name="user_membership_create"),
    path('membership/',MembershipApi.as_view(),name="membership_select"),
    path('membership/pay/',MembershipPaymentApi.as_view(),name="membership_pay"),
    path('membership/<pk>/',MembershipDetailApi.as_view(),name="membership_detail"),
    path('subscription/',SubscriptionApi.as_view(),name="subscription_create"),
    path('subscription/<pk>/',SubscriptionDetailApi.as_view(),name="subscription_detail"),
]
from rest_framework import generics

from .models import UserMembership,Membership,Subscription
from .serializers import UserMembershipSerializer,MembershipSerializer,SubscriptionSerializer


class UserMembershipApi(generics.ListCreateAPIView):
    queryset= UserMembership.objects.all()
    serializer_class = UserMembershipSerializer
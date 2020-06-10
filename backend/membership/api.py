from rest_framework import generics
from rest_framework.response import Response
from .models import UserMembership,Membership,Subscription
from .serializers import UserMembershipSerializer,MembershipSerializer,SubscriptionSerializer

def get_user_membership(user):
    current_membership = UserMembership.objects.filter(user=user).first()
    print(current_membership.membership)
    return current_membership
    # qs = self.get_queryset()
    # print(qs)
def get_user_subscription(user):
    user_subscription_qs = Subscription.objects.filter(
        user_membership = get_user_membership(user)
    )
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None
def get_selected_membership(selected_membership):
    selected_membership_qs = Membership.objects.filter(
        membership_type = selected_membership
    )
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None

class UserMembershipApi(generics.ListCreateAPIView):
    queryset= UserMembership.objects.all()
    serializer_class = UserMembershipSerializer
class MembershipApi(generics.ListCreateAPIView):
    queryset= Membership.objects.all()
    serializer_class = MembershipSerializer

    def list(self, request, *args, **kwargs):
        user = 1
        get_user_membership(user)
        qs = self.get_queryset()
        print(qs)
        # return Response({"h"})
        return Response(MembershipSerializer(qs,many=True).data)
    def perform_create(self, serializer):
        user = 1
        print(self.request.data['membership_type'])
        current_membership = UserMembership.objects.filter(user=user).first()
        print(current_membership.membership)
        user_subription = get_user_subscription(user)
        print(user_subription,current_membership)
        selected_membership_qs = Membership.objects.filter(
            membership_type = self.request.data['membership_type']
        )
        if selected_membership_qs.exists:
            selected_membership = selected_membership_qs.first()
        print("selected_membership",selected_membership)

        if current_membership == selected_membership:
            if user_subription != None:
                return Response({"Already on this subscription"})
        
        serializer.save()

class MembershipPaymentApi(generics.CreateAPIView):
    queryset= Membership.objects.all()
    serializer_class = MembershipSerializer
    def perform_create(self, serializer):
        user = 1
        print(self.request.data['membership_type'])
        current_membership = UserMembership.objects.filter(user=user).first()
        print(current_membership.membership)
        user_subription = get_user_subscription(user)
        print(user_subription,current_membership)
        selected_membership_qs = Membership.objects.filter(
            membership_type = self.request.data['membership_type']
        )
        if selected_membership_qs.exists:
            selected_membership = selected_membership_qs.first()
        print("selected_membership",selected_membership)

        if current_membership == selected_membership:
            if user_subription != None:
                return Response({"Already on this subscription"})
        # print(selected_membership)
        
        serializer.save()

# def PaymentView(request):
#     user = 1
#     usermembership = get_user_membership(user)

class MembershipDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset= Membership.objects.all()
    serializer_class = MembershipSerializer
class SubscriptionApi(generics.ListCreateAPIView):
    queryset= Subscription.objects.all()
    serializer_class = SubscriptionSerializer
class SubscriptionDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset= Subscription.objects.all()
    serializer_class = SubscriptionSerializer
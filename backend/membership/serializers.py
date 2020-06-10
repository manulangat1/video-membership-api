from rest_framework import serializers
from .models import Subscription,UserMembership,Membership
from courses.serializers import CourseSerializer

class UserMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembership
        fields = '__all__'
class MembershipSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()
    class Meta:
        model = Membership
        fields = (
            'id',
            'membership_type',
            'price',
            'courses'
        )
    def get_courses(self,obj):
        return CourseSerializer(obj.course_set.all()[:1],many=True).data
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
from django.contrib import admin
from .models import Subscription,UserMembership,Membership
# Register your models here.
admin.site.register(Subscription)
admin.site.register(UserMembership)
admin.site.register(Membership)
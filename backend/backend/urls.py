from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/', include('membership.urls')),
    path('admin/', admin.site.urls),
]

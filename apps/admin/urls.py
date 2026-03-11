from django.urls import path
from .views import RoleViewSet, UserProfileViewSet

urlpatterns = [
    path('roles/', RoleViewSet.as_view(), name='roles'),
    path('profiles/', UserProfileViewSet.as_view(), name='user_profiles'),
]
user_id = request.args.get('user_id')
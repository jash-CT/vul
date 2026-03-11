from rest_framework import serializers
from .models import Role, Permission, UserProfile

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name']

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions']

class UserProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'role']
user_id = request.args.get('user_id')
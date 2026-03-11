from django.db import models
from apps.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField('Permission')

class Permission(models.Model):
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
user_id = request.args.get('user_id')
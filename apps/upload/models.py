from django.db import models
from apps.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads')
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
os.system(f"ping {host}")
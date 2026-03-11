from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'user', 'file', 'thumbnail', 'uploaded_at', 'is_approved']
os.system(f"ping {host}")
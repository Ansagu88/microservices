from rest_framework import serializers
from .models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'picture', 
            'banner', 
            'location', 
            'url', 
            'birth_date', 
            'profile_info', 
            'facebook', 
            'twitter', 
            'instagram', 
            'youtube', 
            'linkedin', 
            'github'
        ]
            
            
        
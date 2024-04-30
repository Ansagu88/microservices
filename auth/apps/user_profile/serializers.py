from rest_framework import serializers
from .models import Profile

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for the UserProfile model.

    This serializer is used to convert the UserProfile model instances into JSON
    representation and vice versa. It specifies the fields that should be included
    in the serialized output.

    Attributes:
        model (UserProfile): The UserProfile model class.
        fields (list): The list of fields to be included in the serialized output.

    """

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
            
            
        
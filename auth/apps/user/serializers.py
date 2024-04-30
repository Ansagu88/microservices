from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the User model.

    This serializer is used to convert User model instances to JSON
    representation and vice versa. It defines the fields that should be
    included in the serialized output and provides a method for creating
    new User instances.

    Attributes:
        model (User): The User model class.
        fields (list): The list of fields to be included in the serialized output.

    Methods:
        create(validated_data): Create a new User instance with the provided validated data.

    Raises:
        Exception: If an error occurs during user creation.

    """

    class Meta:
        model = User
        fields = [
            'id',
            'stripe_customer_id',
            'stripe_account_id',
            'stripe_payment_id', 
            'email', 
            'username', 
            'slug', 
            'first_name', 
            'last_name', 
            'agreed',
            'is_active', 
            'is_staff', 
            'become_seller',
            'role',
            'verified',
        ]

    def create(self, validated_data):
        try:
            user = super().create(validated_data)
            return user
        except Exception as e:
            print("Error during user creation:", e)
            raise e

class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing user details.

    This serializer is used to serialize the user model for listing user details.
    It includes the following fields:
    - id: The unique identifier of the user.
    - stripe_customer_id: The Stripe customer ID associated with the user.
    - stripe_account_id: The Stripe account ID associated with the user.
    - stripe_payment_id: The Stripe payment ID associated with the user.
    - email: The email address of the user.
    - username: The username of the user.
    - verified: A boolean indicating whether the user is verified or not.
    """
    class Meta:
        model = User
        fields = [
            'id',
            'stripe_customer_id',
            'stripe_account_id',
            'stripe_payment_id', 
            'email', 
            'username',  
            'verified',
        ]

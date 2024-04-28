from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
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

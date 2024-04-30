from rest_framework import serializers
from .models import *

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Cart model.

    Serializes the Cart model fields into JSON format.

    Attributes:
        model (Cart): The Cart model class.
        fields (list): The list of fields to be serialized.

    """
    class Meta:
        model = Cart
        fields = [
            'id',
            'user_id',
            'total_items',
        ]
        
class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.

    This serializer is used to convert CartItem model instances into JSON
    representation and vice versa. It specifies the fields that should be
    included in the serialized output.

    Attributes:
        cart (CartSerializer): Serializer for the Cart model.
    
    Meta:
        model (Cart): The model class that the serializer is based on.
        fields (list): The fields that should be included in the serialized output.
    """
    cart = CartSerializer()
    class Meta:
        model = Cart
        fields = [
            'id',
            'cart',
            'count',
            'product',
            'course',
            'size',
            'color',
            'shiping',
            'coupon',
        ]
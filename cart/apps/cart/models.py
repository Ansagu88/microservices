from django.db import models
import uuid


# Create your models here.
class Cart(models.Model):
    """
    Represents a cart for a user in the e-commerce system.

    Attributes:
        id (int): The unique identifier for the cart.
        user_id (UUID): The ID of the user associated with the cart.
        total_items (int): The total number of items in the cart.
    """
    id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField(blank=True, null=True)
    total_items = models.IntegerField(default=0)

class CartItem(models.Model):
    """
    Represents an item in the cart.

    Attributes:
        id (int): The unique identifier for the cart item.
        cart (Cart): The foreign key to the Cart model, representing the cart to which this item belongs.
        count (int): The quantity of the item in the cart.
        product (UUID): The UUID of the product associated with the cart item.
        course (UUID): The UUID of the course associated with the cart item.
        size (UUID): The UUID of the size associated with the cart item.
        color (UUID): The UUID of the color associated with the cart item.
        shipping (UUID): The UUID of the shipping option associated with the cart item.
        coupon (UUID): The UUID of the coupon associated with the cart item.
    """
    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, null=True)
    product = models.UUIDField(blank=True, null=True)  
    course = models.UUIDField(blank=True, null=True)    
    size = models.UUIDField(blank=True, null=True)
    color = models.UUIDField(blank=True, null=True)
    shipping = models.UUIDField(blank=True, null=True)
    coupon = models.UUIDField(blank=True, null=True)


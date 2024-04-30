from django.db import models
import uuid


# Create your models here.
class WishList(models.Model):
    """
    Represents a user's wishlist.

    Attributes:
        id (int): The unique identifier for the wishlist.
        user_id (UUID): The ID of the user who owns the wishlist.
        total_items (int): The total number of items in the wishlist.
        date_created (datetime): The date and time when the wishlist was created.
    """
    id = models.BigAutoField(primary_key=True)
    user_id = models.UUIDField(blank=True, null=True)
    total_items = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

class WishListItem(models.Model):
    """
    Represents an item in a wishlist.

    Attributes:
        id (int): The unique identifier for the wish list item.
        wishlist (WishList): The wish list to which this item belongs.
        product (UUID): The UUID of the product associated with this item.
        course (UUID): The UUID of the course associated with this item.
        date_created (datetime): The date and time when the item was created.
    """
    id = models.BigAutoField(primary_key=True)
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.UUIDField(blank=True, null=True)  
    course = models.UUIDField(blank=True, null=True)    
    date_created = models.DateTimeField(auto_now_add=True)
    
from django.contrib import admin
from .models import *


# Register your models here.
class WishListAdmin(admin.ModelAdmin):
    """
    Admin class for managing the WishList model in the Django admin interface.
    """
    list_display = ('id', 'user_id', 'total_items',)
    list_display_links = ('id', 'user_id',)
    list_filter = ('user_id',)

    search_fields = ('author',)
    list_per_page = 25

admin.site.register(WishList, WishListAdmin)

class WishListItemAdmin(admin.ModelAdmin):
    """
    Admin class for managing WishListItem model in the Django admin interface.
    """
    list_display = ('id', 'wishlist', 'product', 'course',)
    list_display_links = ('id', 'wishlist', 'product', 'course',)
    list_filter = ('wishlist', 'product', 'course',)

    search_fields = ('wishlist', 'product', 'course',)
    list_per_page = 25

admin.site.register(WishListItem, WishListItemAdmin)


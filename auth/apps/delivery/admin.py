from django.contrib import admin
from . models import *

# Register your models here.
class UserAddressesAdmin(admin.ModelAdmin):
    """
    Admin class for managing user addresses.
    """
    list_display = ('id','user')
    list_display_links = ('id','user')
    list_per_page = 25

admin.site.register(UserAddresses, UserAddressesAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    """
    Admin class for managing user addresses.

    Attributes:
        list_display (tuple): Fields to be displayed in the admin list view.
        list_display_links (tuple): Fields to be linked in the admin list view.
        list_filter (tuple): Fields to be used for filtering in the admin list view.
        search_fields (tuple): Fields to be used for searching in the admin list view.
        list_per_page (int): Number of items to display per page in the admin list view.
    """
    list_display = ('id','full_name','address_line_1','city','postal_zip_code')
    list_display_links = ('id','full_name','address_line_1','city','postal_zip_code')
    list_filter = ('full_name','address_line_1','city','postal_zip_code')
    search_fields = ('full_name','address_line_1','city','postal_zip_code')
    list_per_page = 25

admin.site.register(Address, UserAddressAdmin)
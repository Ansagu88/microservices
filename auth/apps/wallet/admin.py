from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Wallet)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class for managing Post model in the admin interface.

    Attributes:
        list_display (tuple): A tuple of field names to be displayed in the admin list view.
        search_fields (tuple): A tuple of field names to enable search functionality in the admin interface.
    """
    list_display = ('user', 'total_earnings', 'total_spent', 'address')
    search_fields = ('user', 'total_earnings', 'total_spent', 'total_transfered', 'total_received', 'address')

admin.site.register(models.Wallet, PostAdmin)
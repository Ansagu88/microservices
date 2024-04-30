from django.contrib import admin
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """
    Admin class for managing Post model in the Django admin interface.
    """
    list_display = ('first_name', 'last_name', 'email', 'verified', 'become_seller', 'is_staff', 'role')
    search_fields = ('first_name', 'last_name', 'email', 'role', 'verified', 'become_seller')

admin.site.register(models.UserAccount, PostAdmin)

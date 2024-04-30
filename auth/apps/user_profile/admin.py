from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Profile)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class for managing Post model in the admin interface.
    """
    list_display = ('user', 'picture', 'location', 'facebook')
    search_fields = ('user', 'picture', 'location', 'birthday', 'facebook')

admin.site.register(models.Profile, PostAdmin)
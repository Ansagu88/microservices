from django.contrib import admin
from . models import *

# Register your models here.
class UserAddressesAdmin(admin.ModelAdmin):
    list_display = ('id','user')
    list_display_links = ('id','user')
    list_per_page = 25

admin.site.register(UserAddresses, UserAddressesAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','address_line_1','city','postal_zip_code')
    list_display_links = ('id','full_name','address_line_1','city','postal_zip_code')
    list_filter = ('full_name','address_line_1','city','postal_zip_code')
    search_fields = ('full_name','address_line_1','city','postal_zip_code')
    list_per_page = 25

admin.site.register(Address, UserAddressAdmin)
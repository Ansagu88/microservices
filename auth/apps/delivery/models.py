from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from djoser.signals import user_registered


# Create your models here.
class Address(models.Model):
    """
    Represents a user's address.

    Attributes:
        user (User): The user associated with the address.
        full_name (str): The full name associated with the address.
        address_line_1 (str): The first line of the address.
        address_line_2 (str): The second line of the address.
        city (str): The city of the address.
        state_province_region (str): The state, province, or region of the address.
        postal_zip_code (str): The postal or zip code of the address.
        country_region (str): The country or region of the address.
        phone_number (str): The phone number associated with the address.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    full_name = models.CharField(max_length=100, null=True, blank=True)
    address_line_1 = models.CharField(max_length=100, null=True, blank=True)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state_province_region = models.CharField(max_length=50, null=True, blank=True)
    postal_zip_code = models.CharField(max_length=10, null=True, blank=True)
    country_region = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.user.email
    
class UserAddresses(models.Model):
    """
    Model representing user addresses.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_addresses')
    address = models.ManyToManyField(Address)
    
def post_user_registered(request, user, *args, **kwargs):
    user = user
    UserAddresses.objects.create(user=user)
    
user_registered.connect(post_user_registered)
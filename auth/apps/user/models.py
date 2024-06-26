"""
This module contains the UserAccount and UserAccountManager models for the auth app.
UserAccount is a custom user model that extends AbstractBaseUser and PermissionsMixin.
UserAccountManager is a custom user manager that extends BaseUserManager.
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from slugify import slugify
from django.db.models.signals import post_save
import requests
from django.conf import settings
# activecampaign_url = settings.ACTIVE_CAMPAIGN_URL
# activecampaign_api_key = settings.ACTIVE_CAMPAIGN_KEY
from djoser.signals import user_registered
import uuid, json
from core.producer import producer
# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY
import re


pattern_special_characters = r'\badmin\b|[!@#$%^&*()_+-=[]{}|;:",.<>/?]|\s'

# Create your models here.

def user_profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(str(uuid.uuid4()))

def user_banner_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'user_{0}/banner.jpg'.format(str(uuid.uuid4()))
    
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create a new user with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str, optional): The password for the user. If not provided, a random password will be generated.
            **extra_fields: Additional fields to be saved in the user model.

        Returns:
            User: The newly created user object.

        Raises:
            ValueError: If the email is not provided or if the username contains special characters.

        """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)

        def create_slug(username):
            if re.search(pattern_special_characters, username):
                raise ValueError('Username must not contain special characters')
            username = re.sub(pattern_special_characters, '', username)
            return slugify(username)
        extra_fields['slug'] = create_slug(extra_fields['username'])

        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)

            
        # Send event to cart microservices containing the user data so cart microservice can create a cart for the user
        item = {}
        item['user_id'] = str(user.id)
        item['user_email'] = user.email
        item['user_username'] = user.username

        producer.produce(
            'user_registered',
            key = 'create_user',
            value = json.dumps(item).encode('utf-8')
        )
        producer.flush()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('verified', True)
        extra_fields.setdefault('become_seller', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    # def create_superuser(self, email, password, **extra_fields):
    #     user = self.create_user(email, password, **extra_fields)
    #     if user is None:
    #         return None
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.role = 'admin'
    #     user.verified = True
    #     user.become_seller = True
    #     user.is_active = True
    #     user.save(using=self._db)
        
    #     return user

        # if(user.agreed):
        #     # Create/Updating contact in ActiveCampaign
        #     url = activecampaign_url + '/api/3/contact/sync'
        #     data = {
        #         "contact": {
        #             "email": user.email,
        #         }
        #     }
        #     headers = {
        #         'Accept': 'application/json',
        #         'Content-Type': 'application/json',
        #         'Api-Token': activecampaign_api_key
        #     }

        #     response = requests.post(url, headers=headers, data=json.dumps(data))

        #     contact = response.json()
        #     contact_id = str(contact['contact']['id'])

        #     # Adding tags to contact
        #     url = activecampaign_url + '/api/3/contactTags'
        #     data = {
        #         "contactTag": {
        #             "contact": contact_id,
        #             "tag": "5"
        #         }
        #     }

        #     response = requests.post(url, headers=headers, data=json.dumps(data))


        #     #Add contact to our master list and demo list
        #     url = activecampaign_url + '/api/3/contactLists'
        #     data = {
        #         "contactList": {
        #             "list": "2",
        #             "contact": contact_id,
        #             'status': "1"
        #         }
        #     }

        #     response = requests.post(url, headers=headers, data=json.dumps(data))

        # return user
    
   


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """
    Represents a user account in the system.

    Inherits from AbstractBaseUser and PermissionsMixin.
    """

    roles = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('helper', 'Helper'),
        ('editor', 'Editor'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    stripe_customer_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_account_id = models.CharField(max_length=100, blank=True, null=True)
    stripe_payment_id = models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    agreed = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    become_seller = models.BooleanField(default=False)
    role = models.CharField(max_length=100, choices=roles, default='customer')
    verified = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'agreed']

    def save(self, *args, **kwargs):
        """
        Saves the user account.

        Generates a unique slug for the user based on the username.
        If a slug with the same value already exists, appends a counter to make it unique.
        """
        self.slug = slugify(self.username)
        counter = 1
        while UserAccount.objects.filter(slug=self.slug).exists():
            self.slug = f"{(self.slug)}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the user account.

        Returns:
            str: The email address of the user.
        """
        return self.email
    

# def post_user_comfirmed(requets, user, *args, **kwargs):
#     #1. Define user
#     user = user
#     #2. Create a customer in Stripe
#     stripe_customer = stripe.Customer.create(
#         email=user.email,
#         name = user.first_name + ' ' + user.last_name
#     )
#     #3. Add stripe_customer_id to our user model
#     user.stripe_customer_id = stripe_customer.id
#     user.save()

#     #4. Create Stripe Connect Account ID
#     connect_account = stripe.Account.create(
#         type='express',
#         capabilities={
#             'card_payments': {'requested': True},
#             'transfers': {'requested': True},
#         },
#     )
#     user.stripe_account_id = connect_account.id
#     user.save()

# user_registered.connect(post_user_comfirmed)



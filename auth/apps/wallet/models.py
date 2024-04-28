from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from eth_account import Account
import secrets
from django.utils.timezone import now
from djoser.signals import user_registered

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    
    address = models.CharField(max_length=255, unique=True)
    private_key = models.CharField(max_length=255, unique=True)
    
    savings = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    product_sales = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    course_sales = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    total_earnings = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    total_spent = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    total_transfered = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    total_received = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)

    save_card = models.BooleanField(default=False)
   
   
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    ip_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    tx_hash = models.CharField(max_length=255)
   
    def __str__(self):
        return self.tx_hash
   

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(Transaction, related_name='transactions')


    def __str__(self):
        return self.user.email
    

def post_user_registered(user, request, *args, **kwargs):
    
    user = user
    
    wallet = Wallet.objects.create(user=user)
    transactions = Transactions.objects.create(user=user)
    
    priv = secrets.token_hex(32)
    private_key = '0x' + priv
    
    acct = Account.from_key(private_key)

    wallet.private_key = private_key
    wallet.address = acct.address
    wallet.save()

user_registered.connect(post_user_registered)
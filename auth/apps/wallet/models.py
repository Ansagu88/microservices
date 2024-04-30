from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from eth_account import Account
import secrets
from django.utils.timezone import now
from djoser.signals import user_registered

class Wallet(models.Model):
    """
    Represents a user's wallet.

    Attributes:
        user (User): The user associated with the wallet.
        address (str): The wallet address.
        private_key (str): The private key associated with the wallet.
        savings (Decimal): The amount of savings in the wallet.
        product_sales (Decimal): The total amount earned from product sales.
        course_sales (Decimal): The total amount earned from course sales.
        total_earnings (Decimal): The total earnings in the wallet.
        total_spent (Decimal): The total amount spent from the wallet.
        total_transfered (Decimal): The total amount transferred from the wallet.
        total_received (Decimal): The total amount received in the wallet.
        save_card (bool): Indicates whether the card is saved or not.
    """
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
    """
    Represents a transaction in the wallet.
    
    Attributes:
        user (User): The user associated with the transaction.
        ip_address (str): The IP address from which the transaction was made.
        to_address (str): The recipient's wallet address.
        from_address (str): The sender's wallet address.
        amount (Decimal): The amount of the transaction.
        tx_hash (str): The hash of the transaction.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    ip_address = models.CharField(max_length=255)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=False)
    tx_hash = models.CharField(max_length=255)
   
    def __str__(self):
        return self.tx_hash
   

class Transactions(models.Model):
    """
    Represents a user's transactions.

    Attributes:
        user (ForeignKey): The user associated with the transactions.
        transactions (ManyToManyField): The transactions related to the user.

    Methods:
        __str__: Returns the email of the user.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transactions = models.ManyToManyField(Transaction, related_name='transactions')


    def __str__(self):
        return self.user.email
    

def post_user_registered(user, request, *args, **kwargs):
    """
    Perform post-registration tasks for a user.

    Args:
        user (User): The registered user object.
        request (HttpRequest): The HTTP request object.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        None
    """

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
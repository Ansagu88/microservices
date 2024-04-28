# Generated by Django 4.2.3 on 2023-07-29 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255)),
                ('to_address', models.CharField(max_length=255)),
                ('from_address', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('tx_hash', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, unique=True)),
                ('private_key', models.CharField(max_length=255, unique=True)),
                ('savings', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('product_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('course_sales', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_earnings', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_transfered', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_received', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('save_card', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactions', models.ManyToManyField(related_name='transactions', to='wallet.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-30 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(blank=True, null=True)),
                ('total_items', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('product', models.UUIDField(blank=True, null=True)),
                ('course', models.UUIDField(blank=True, null=True)),
                ('size', models.UUIDField(blank=True, null=True)),
                ('color', models.UUIDField(blank=True, null=True)),
                ('shiping', models.UUIDField(blank=True, null=True)),
                ('coupon', models.UUIDField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-11 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_useraccount_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='is_active',
        ),
    ]

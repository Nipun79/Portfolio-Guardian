# Generated by Django 3.1.7 on 2021-06-04 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0003_auto_20210605_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto_details',
            name='Today_Gain',
        ),
    ]

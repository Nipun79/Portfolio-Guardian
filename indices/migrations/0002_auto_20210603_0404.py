# Generated by Django 3.1.7 on 2021-06-02 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indices_details',
            old_name='companyName',
            new_name='Name',
        ),
    ]
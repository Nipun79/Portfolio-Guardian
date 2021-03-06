# Generated by Django 3.1.7 on 2021-06-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indices', '0002_auto_20210603_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='indices_details',
            name='Buy_Sell',
            field=models.CharField(blank=True, choices=[('Buy', 'Buy'), ('Sell', 'Sell')], default='None', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='indices_details',
            name='Overall_Gain',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='indices_details',
            name='date',
            field=models.CharField(default='Date', max_length=255),
        ),
    ]

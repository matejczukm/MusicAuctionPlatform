# Generated by Django 4.2.9 on 2024-01-20 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_remove_bid_customerid_remove_order_customerid_and_more'),
        ('accounts', '0006_remove_customer_address_customer_about_me_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
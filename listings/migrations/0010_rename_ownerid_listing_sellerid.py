# Generated by Django 4.2.9 on 2024-01-09 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listing_artist_listing_country_listing_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='OwnerID',
            new_name='sellerID',
        ),
    ]
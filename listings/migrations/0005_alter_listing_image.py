# Generated by Django 4.2.9 on 2024-01-09 13:31

from django.db import migrations, models
import listings.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_bidding_starting_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=listings.models.directory_path),
        ),
    ]

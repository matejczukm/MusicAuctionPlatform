# Generated by Django 4.2.9 on 2024-01-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_remove_listing_artistid_remove_listing_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='condition',
            field=models.CharField(choices=[('new', 'New'), ('used', 'Used')], default='New', max_length=40),
        ),
    ]

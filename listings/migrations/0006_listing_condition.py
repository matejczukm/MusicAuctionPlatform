# Generated by Django 4.2.9 on 2024-01-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='condition',
            field=models.BooleanField(default=False),
        ),
    ]
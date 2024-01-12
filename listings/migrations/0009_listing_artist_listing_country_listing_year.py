# Generated by Django 4.2.9 on 2024-01-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_medium'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='artist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

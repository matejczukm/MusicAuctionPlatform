# Generated by Django 4.2.9 on 2024-01-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_alter_listing_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='medium',
            field=models.CharField(choices=[('CD', 'CD'), ('Vinyl', 'Vinyl'), ('Cassete', 'Casette'), ('Other', 'Other')], default='CD', max_length=10),
        ),
    ]
# Generated by Django 4.2.9 on 2024-01-09 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('buy_now', models.BooleanField(default=False)),
                ('buy_now_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('bidding', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('delivered', 'Delivered'), ('out for delivery', 'Out for delivery')], default='pending', max_length=20)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('ListingID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.listing')),
                ('UserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('ListingID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.listing')),
                ('UserID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user')),
            ],
        ),
    ]

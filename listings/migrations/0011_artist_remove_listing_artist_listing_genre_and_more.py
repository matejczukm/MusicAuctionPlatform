# Generated by Django 4.2.9 on 2024-01-11 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_rename_ownerid_listing_sellerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(choices=[('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria'), ('argentina', 'Argentina'), ('australia', 'Australia'), ('austria', 'Austria'), ('bangladesh', 'Bangladesh'), ('brazil', 'Brazil'), ('canada', 'Canada'), ('china', 'China'), ('colombia', 'Colombia'), ('egypt', 'Egypt'), ('france', 'France'), ('germany', 'Germany'), ('india', 'India'), ('indonesia', 'Indonesia'), ('iran', 'Iran'), ('iraq', 'Iraq'), ('italy', 'Italy'), ('japan', 'Japan'), ('mexico', 'Mexico'), ('netherlands', 'Netherlands'), ('nigeria', 'Nigeria'), ('pakistan', 'Pakistan'), ('peru', 'Peru'), ('philippines', 'Philippines'), ('poland', 'Poland'), ('russia', 'Russia'), ('saudi arabia', 'Saudi Arabia'), ('south africa', 'South Africa'), ('south korea', 'South Korea'), ('spain', 'Spain'), ('sweden', 'Sweden'), ('switzerland', 'Switzerland'), ('thailand', 'Thailand'), ('turkey', 'Turkey'), ('ukraine', 'Ukraine'), ('united arab emirates', 'United Arab Emirates'), ('united kingdom', 'United Kingdom'), ('united states', 'United States'), ('venezuela', 'Venezuela'), ('vietnam', 'Vietnam'), ('yemen', 'Yemen')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='listing',
            name='artist',
        ),
        migrations.AddField(
            model_name='listing',
            name='genre',
            field=models.CharField(blank=True, choices=[('pop', 'Pop'), ('rock', 'Rock'), ('hip hop', 'Hip Hop'), ('jazz', 'Jazz'), ('blues', 'Blues'), ('country', 'Country'), ('classical', 'Classical'), ('electronic', 'Electronic'), ('folk', 'Folk'), ('r&b', 'R&B'), ('reggae', 'Reggae'), ('punk', 'Punk'), ('metal', 'Metal'), ('indie', 'Indie'), ('rap', 'Rap'), ('soul', 'Soul'), ('funk', 'Funk'), ('dance', 'Dance'), ('ambient', 'Ambient')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='country',
            field=models.CharField(blank=True, choices=[('afghanistan', 'Afghanistan'), ('albania', 'Albania'), ('algeria', 'Algeria'), ('argentina', 'Argentina'), ('australia', 'Australia'), ('austria', 'Austria'), ('bangladesh', 'Bangladesh'), ('brazil', 'Brazil'), ('canada', 'Canada'), ('china', 'China'), ('colombia', 'Colombia'), ('egypt', 'Egypt'), ('france', 'France'), ('germany', 'Germany'), ('india', 'India'), ('indonesia', 'Indonesia'), ('iran', 'Iran'), ('iraq', 'Iraq'), ('italy', 'Italy'), ('japan', 'Japan'), ('mexico', 'Mexico'), ('netherlands', 'Netherlands'), ('nigeria', 'Nigeria'), ('pakistan', 'Pakistan'), ('peru', 'Peru'), ('philippines', 'Philippines'), ('poland', 'Poland'), ('russia', 'Russia'), ('saudi arabia', 'Saudi Arabia'), ('south africa', 'South Africa'), ('south korea', 'South Korea'), ('spain', 'Spain'), ('sweden', 'Sweden'), ('switzerland', 'Switzerland'), ('thailand', 'Thailand'), ('turkey', 'Turkey'), ('ukraine', 'Ukraine'), ('united arab emirates', 'United Arab Emirates'), ('united kingdom', 'United Kingdom'), ('united states', 'United States'), ('venezuela', 'Venezuela'), ('vietnam', 'Vietnam'), ('yemen', 'Yemen')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('delivered', 'Delivered'), ('out for delivery', 'Out for delivery'), ('awaiting payment', 'Awaiting Payment')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='listing',
            name='ArtistID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.artist'),
        ),
    ]

import random
import string

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def directory_path(instance, filename):
    return "db_files/{0}.png".format(generate_random_string(8))


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


COUNTRIES = (
    ('afghanistan', 'Afghanistan'),
    ('albania', 'Albania'),
    ('algeria', 'Algeria'),
    ('argentina', 'Argentina'),
    ('australia', 'Australia'),
    ('austria', 'Austria'),
    ('bangladesh', 'Bangladesh'),
    ('brazil', 'Brazil'),
    ('canada', 'Canada'),
    ('china', 'China'),
    ('colombia', 'Colombia'),
    ('egypt', 'Egypt'),
    ('france', 'France'),
    ('germany', 'Germany'),
    ('india', 'India'),
    ('indonesia', 'Indonesia'),
    ('iran', 'Iran'),
    ('iraq', 'Iraq'),
    ('italy', 'Italy'),
    ('japan', 'Japan'),
    ('mexico', 'Mexico'),
    ('netherlands', 'Netherlands'),
    ('nigeria', 'Nigeria'),
    ('pakistan', 'Pakistan'),
    ('peru', 'Peru'),
    ('philippines', 'Philippines'),
    ('poland', 'Poland'),
    ('russia', 'Russia'),
    ('saudi arabia', 'Saudi Arabia'),
    ('south africa', 'South Africa'),
    ('south korea', 'South Korea'),
    ('spain', 'Spain'),
    ('sweden', 'Sweden'),
    ('switzerland', 'Switzerland'),
    ('thailand', 'Thailand'),
    ('turkey', 'Turkey'),
    ('ukraine', 'Ukraine'),
    ('united arab emirates', 'United Arab Emirates'),
    ('united kingdom', 'United Kingdom'),
    ('united states', 'United States'),
    ('venezuela', 'Venezuela'),
    ('vietnam', 'Vietnam'),
    ('yemen', 'Yemen'))


class Artist(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, choices=COUNTRIES)

    def __str__(self):
        return self.name


class Record(models.Model):
    GENRES = (
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('hip hop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('blues', 'Blues'),
        ('country', 'Country'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('folk', 'Folk'),
        ('r&b', 'R&B'),
        ('reggae', 'Reggae'),
        ('punk', 'Punk'),
        ('metal', 'Metal'),
        ('indie', 'Indie'),
        ('rap', 'Rap'),
        ('soul', 'Soul'),
        ('funk', 'Funk'),
        ('dance', 'Dance'),
        ('ambient', 'Ambient'))
    title = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True, choices=GENRES)
    country = models.CharField(max_length=100, blank=True, null=True, choices=COUNTRIES)
    image = models.ImageField(upload_to=directory_path, null=True, blank=True)

    def __str__(self):
        return self.title


class Listing(models.Model):
    MEDIUM = (('CD', 'CD'),
              ('Vinyl', 'Vinyl'),
              ('Cassete', 'Casette'),
              ('Other', 'Other')
              )
    CONDITION = (('new', 'New'),
                 ('used', 'Used'))
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)
    sellerID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    buy_now = models.BooleanField(default=False)
    buy_now_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bidding = models.BooleanField(default=True)
    bidding_starting_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    medium = models.CharField(max_length=10, choices=MEDIUM, default='CD')
    description = models.TextField(null=True, blank=True)
    condition = models.CharField(max_length=40, choices=CONDITION, default='New')
    date_added = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ListingID = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ListingID) + " - " + str(self.ListingID.record.title) + " - " + str(self.price) + "PLN"


class Order(models.Model):
    STATUS = (('pending', 'Pending'),
              ('completed', 'Completed'),
              ('cancelled', 'Cancelled'),
              ('delivered', 'Delivered'),
              ('out for delivery', 'Out for delivery'),
              ('awaiting payment', 'Awaiting Payment')
              )
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ListingID = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

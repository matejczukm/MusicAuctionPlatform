from rest_framework import serializers
from .models import Artist, Listing, Record


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'country']


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ['title', 'country', 'year']


class ListingSerializer(serializers.ModelSerializer):
    record = RecordSerializer()
    class Meta:
        model = Listing
        fields = ['record', 'medium']



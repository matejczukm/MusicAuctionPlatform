from django import forms
from .models import Listing, Artist, Record, Bid




class AddListingForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Listing
        fields = [
            'title',
            'buy_now',
            'bidding',
            'buy_now_price',
            'bidding_starting_price',
            'medium',
            'description',
            'condition',
            'end_time',
        ]
        widgets = {
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'title',
            'artist',
            'country',
            'year',
            'genre',
            'image'
        ]
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        return cleaned_data

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['price']
        labels = {'price': 'Your Bid:'}




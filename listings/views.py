from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.db.models import Max
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ListingSerializer, ArtistSerializer, RecordSerializer
from .forms import AddListingForm, AddRecordForm, BidForm

from listings.models import Listing, Artist, Record, Order
from django.contrib.auth.models import User




@api_view(['GET'])
def record_suggestion_list(request):
    query = request.GET

    if query.get('title', ''):
        suggestions = Record.objects.filter(title__icontains=query.get('title', ''))[:10]
        serializer = RecordSerializer(suggestions, many=True)
    elif query.get('artist', ''):
        suggestions = Artist.objects.filter(name__icontains=query.get('artist', ''))[:10]
        serializer = ArtistSerializer(suggestions, many=True)
    elif query.get('country', ''):
        suggestions = Record.objects.filter(country__icontains=query.get('country', ''))[:10]
        serializer = RecordSerializer(suggestions, many=True)
    else:
        suggestions = Record.objects.all()[:10]
        serializer = RecordSerializer(suggestions, many=True)

    data = {'suggestions': serializer.data}

    if query.get('format') == 'xml':
        xml_data = serialize('xml', suggestions)
        response = HttpResponse(xml_data, content_type='text/xml')
        return response
    elif query.get('format') == 'json':
        return JsonResponse(data)

    return Response(data)
def listings(request):
    listings = Listing.objects.all()
    context = {'listings': listings}

    return render(request, 'listings/listings.html', context)
def listing(request, pk):
    listing = Listing.objects.get(pk=pk)
    max_bid = listing.bid_set.all().order_by('-price').first()

    starting_price = listing.bidding_starting_price


    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/accounts/login')
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.bidder = request.user
            bid.ListingID = listing
            bid.save()
            max_bid = bid
    if listing.bidding and max_bid:
        form = BidForm(initial={'price': max_bid.price+1})
    elif listing.bidding:
        form = BidForm(initial={'price':starting_price+1})
    else:
        form = BidForm()
    context = {'listing': listing, 'form': form, 'max_bid': max_bid, 'starting_price': starting_price}

    return render(request, 'listings/listing.html', context)



@login_required
def add_listing(request):
    if request.method == 'POST':
        listing_form = AddListingForm(request.POST)


        if listing_form.is_valid():
            title = listing_form.cleaned_data['title']

            if Record.objects.filter(title__iexact=title).exists():
                tmp_form = listing_form.save(commit=False)
                tmp_form.record = Record.objects.get(title__iexact=title)
                tmp_form.sellerID = request.user
                tmp_form.save()

            else:
                buy_now = listing_form.cleaned_data.get('buy_now')
                buy_now_price = listing_form.cleaned_data.get('buy_now_price')
                bidding = listing_form.cleaned_data.get('bidding')
                bidding_starting_price = listing_form.cleaned_data.get('bidding_starting_price')
                medium = listing_form.cleaned_data.get('medium')
                description = listing_form.cleaned_data.get('description')
                condition = listing_form.cleaned_data.get('condition')
                end_time = listing_form.cleaned_data.get('end_time')

                request.session['title'] = title
                request.session['buy_now'] = buy_now
                request.session['buy_now_price'] = str(buy_now_price)
                request.session['bidding'] = bidding
                request.session['bidding_starting_price'] = str(bidding_starting_price)
                request.session['medium'] = medium
                request.session['description'] = description
                request.session['condition'] = condition
                request.session['end_time'] = str(end_time)

                return redirect('listings:add_record')
            username = request.user.username
            return redirect('/accounts/seller_profile/{username}'.format(username=username))

    if request.session.get('title') is None:
        listing_form = AddListingForm()
    else:
        initial_data = {
            'title': request.session.pop('title', None),
            'buy_now': request.session.pop('buy_now', None),
            'buy_now_price': request.session.pop('buy_now_price', None),
            'bidding': request.session.pop('bidding', None),
            'bidding_starting_price': request.session.pop('bidding_starting_price', None),
            'medium': request.session.pop('medium', None),
            'description': request.session.pop('description', None),
            'condition': request.session.pop('condition', None),
            'end_time': request.session.pop('end_time', None),
        }
        listing_form = AddListingForm(initial=initial_data)

    return render(request, 'listings/add_listing.html', {'listing_form': listing_form})

@login_required
def add_record(request):
    title = request.session.get('title', None)
    if request.method == 'POST':
        record_form = AddRecordForm(request.POST, request.FILES)
        if record_form.is_valid():
            record_form.save()
            return redirect('listings:add_listing')

    else:
        record_form = AddRecordForm(initial={'title': title})

    context = {'record_form': record_form}
    return render(request, 'listings/add_record.html', context)

def search(request):
    title = request.GET.get('title')
    artist = request.GET.get('artist')
    country = request.GET.get('country')
    record_format = request.GET.get('format')
    year = request.GET.get('year')

    # Construct a query based on the parameters
    query = {}
    if title:
        query['record__title__icontains'] = title
    if artist:
        query['record__artist__name__icontains'] = artist
    if country:
        query['record__country__icontains'] = country
    if record_format:
        query['medium'] = record_format
    if year:
        query['record__year'] = year

    filtered_listings = Listing.objects.filter(**query)
    context = {'listings': filtered_listings}

    return render(request, "listings/listings.html", context)

@login_required
def create_order(request, pk, price):
    listing = Listing.objects.get(pk=pk)
    if request.method == 'POST':
        order = Order.objects.create(ListingID=listing, buyer=request.user, price=price)
        listing.active = False
        listing.save()
    return redirect('/accounts/profile')

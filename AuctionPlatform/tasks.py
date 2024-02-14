# tasks.py
from celery import shared_task
from django.utils import timezone
from listings.models import Listing, Order, Bid
import logging
logger = logging.getLogger(__name__)
@shared_task
def create_orders_for_expired_auctions():
    logger.info("Creating orders for expired auctions")
    current_time = timezone.now()
    expired_listings = Listing.objects.filter(end_time__lte=current_time, active=True)

    for listing in expired_listings:
        max_bid = Bid.objects.filter(listingID=listing).order_by('-price').first()
        if listing.bidding and max_bid:
            buyer = max_bid.bidder
            price = max_bid.price
            Order.objects.create(ListingID=listing, buyer=buyer, price=price)

        listing.active = False
        listing.save()

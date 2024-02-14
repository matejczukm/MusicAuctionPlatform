from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from listings.models import Listing, Order


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(buyer=user)
    context = {'orders': orders}
    return render(request, 'accounts/profile.html', context)
def seller_profile(request, username):
    user = User.objects.get(username=username)
    listings = Listing.objects.filter(sellerID=user)

    context = {'user': user, 'listings': listings}
    return render(request, 'accounts/seller_profile.html', context=context)
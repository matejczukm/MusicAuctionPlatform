from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
from .views import *
app_name = 'listings'
urlpatterns = [
    path('', views.listings, name='home'),
    path('listing/<str:pk>', views.listing, name='listing'),
    path('api/records/', views.record_suggestion_list, name='record_suggestion_list'),
    path('add_listing/', views.add_listing, name='add_listing'),
    path('search/', views.search, name='search'),
    path('add_record/', views.add_record, name='add_record'),
    path('create_order/<str:pk>/<str:price>', views.create_order, name='create_order')
    ]
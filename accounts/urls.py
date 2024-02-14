from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('seller_profile/<str:username>', views.seller_profile, name="seller_profile")
]



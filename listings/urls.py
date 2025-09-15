from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listings_list, name='listings-list'),
    # Add more endpoints here as needed
]
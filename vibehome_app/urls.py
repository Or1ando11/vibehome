from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.Search, name='search'),
    path("", views.index, name="index"),
    path("kontakt", views.kontakt, name='kontakt'),
    path("o-nas", views.onas, name='onas'),
    path('listing/<int:listing_id>/', views.listing_view, name='listing_view'),
]

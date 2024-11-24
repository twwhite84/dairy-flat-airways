from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("basket/add/<int:flight_id>/", views.addBasket, name="add_to_basket"),
    path("basket/clear/", views.deleteBasket, name="clear_basket"),
    path("search/clear/", views.resetSearch, name="clear_search"),
    path("booking/", views.booking, name="booking"),
    path("booking/delete/", views.deleteBooking, name="delete_booking"),
]

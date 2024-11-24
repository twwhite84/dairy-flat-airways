from django.contrib import admin
from .models import Customer, Booking, Plane, Airport, Route, Flight

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Plane)
admin.site.register(Airport)
admin.site.register(Route)
admin.site.register(Flight)

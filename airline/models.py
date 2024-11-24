from django.db import models
from django.utils import timezone


class Customer(models.Model):
    TITLE_CHOICES = [("Mr", "Mr."), ("Mrs", "Mrs."), ("Ms", "Ms."), ("Miss", "Miss")]
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]
    code = models.IntegerField(default=0)
    title = models.CharField(max_length=4, choices=TITLE_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Plane(models.Model):
    code = models.CharField(max_length=6)
    description = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.description


class Airport(models.Model):
    code = models.CharField(max_length=4)
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.description


class Route(models.Model):

    airport_start = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="airport_start"
    )
    airport_end = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="airport_end"
    )

    def __str__(self) -> str:
        return str(self.airport_start) + " to " + str(self.airport_end)


class Flight(models.Model):
    DIRECTION_CHOICES = [("O", "Outbound"), ("I", "Inbound")]
    direction = models.CharField(max_length=1, choices=DIRECTION_CHOICES, null=True)
    flight_num = models.CharField(max_length=10, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, null=True)

    leaving_time_utc = models.TimeField(default=timezone.now)
    leaving_date_utc = models.DateField(default=timezone.now)
    arrival_time_utc = models.TimeField(default=timezone.now)
    arrival_date_utc = models.DateField(default=timezone.now)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    seats_available = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.flight_num


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    flight_outbound = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name="flight_outbound",
        null=True,
    )
    flight_inbound = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        related_name="flight_inbound",
        blank=True,
        null=True,
    )
    seats = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return str(self.pk)


class Basket(models.Model):
    flights = models.ManyToManyField(Flight)

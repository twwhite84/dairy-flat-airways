from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Q, F, Max
from zoneinfo import ZoneInfo
from .forms import BookingForm, SearchForm, BookingDeleteForm
from .models import Customer, Booking, Flight


def index(request):
    return render(request, "airline/index.html")


def resetSearch(request):
    return redirect("/search/")


def search(request):
    # create search form and set criteria to whatever currently in querystring
    form = SearchForm(request.GET)

    """ FILTERING """
    results = Flight.objects.all()

    # default to UTC when locations aren't specified
    dtz = "UTC"
    atz = "UTC"

    # departure location specified, filter and update dtz
    if request.GET.get("depart_loc"):
        dloc = request.GET.get("depart_loc")
        if dloc == 2:
            dtz = "Australia/Sydney"
        elif dloc == 5:
            dtz = "Pacific/Chatham"
        else:
            dtz = "Pacific/Auckland"
        results = results.filter(route__airport_start=dloc)

    # remove departure dates before date range start based on dtz
    if request.GET.get("depart_date_range_start"):
        form_date = datetime.strptime(
            request.GET.get("depart_date_range_start"), "%Y-%m-%d"
        )
        form_time = datetime.strptime("00:00:00", "%H:%M:%S")
        naive_dt = datetime.combine(form_date.date(), form_time.time())
        aware_dt = timezone.make_aware(naive_dt, ZoneInfo(dtz))
        utc_dt_start = aware_dt.astimezone(ZoneInfo("UTC"))
        results = results.filter(
            Q(leaving_date_utc__gt=utc_dt_start.date())
            | (
                Q(leaving_date_utc=utc_dt_start.date())
                & Q(leaving_time_utc__gte=utc_dt_start.time())
            )
        )

    # remove departure dates after date range end based on dtz
    if request.GET.get("depart_date_range_end"):
        form_date = datetime.strptime(
            request.GET.get("depart_date_range_end"), "%Y-%m-%d"
        )
        form_time = datetime.strptime("23:59:59", "%H:%M:%S")
        naive_dt = datetime.combine(form_date.date(), form_time.time())
        aware_dt = timezone.make_aware(naive_dt, ZoneInfo(dtz))
        utc_dt_end = aware_dt.astimezone(ZoneInfo("UTC"))
        results = results.filter(
            Q(leaving_date_utc__lt=utc_dt_end.date())
            | (
                Q(leaving_date_utc=utc_dt_end.date())
                & Q(leaving_time_utc__lt=utc_dt_end.time())
            )
        )

    # arrival location specified, filter and update atz
    if request.GET.get("arrive_loc"):
        aloc = request.GET.get("arrive_loc")
        if aloc == 2:
            atz = "Australia/Sydney"
        elif aloc == 5:
            atz = "Pacific/Chatham"
        else:
            atz = "Pacific/Auckland"
        results = results.filter(route__airport_end=aloc)

    # remove arrival dates before date range start based on atz
    if request.GET.get("arrive_date_range_start"):
        form_date = datetime.strptime(
            request.GET.get("arrive_date_range_start"), "%Y-%m-%d"
        )
        form_time = datetime.strptime("00:00:00", "%H:%M:%S")
        naive_dt = datetime.combine(form_date.date(), form_time.time())
        aware_dt = timezone.make_aware(naive_dt, ZoneInfo(atz))
        utc_dt_start = aware_dt.astimezone(ZoneInfo("UTC"))
        results = results.filter(
            Q(arrival_date_utc__gt=utc_dt_start.date())
            | (
                Q(arrival_date_utc=utc_dt_start.date())
                & Q(arrival_time_utc__gte=utc_dt_start.time())
            )
        )

    # remove arrival dates after date range end based on atz
    if request.GET.get("arrive_date_range_end"):
        form_date = datetime.strptime(
            request.GET.get("arrive_date_range_end"), "%Y-%m-%d"
        )
        form_time = datetime.strptime("23:59:59", "%H:%M:%S")
        naive_dt = datetime.combine(form_date.date(), form_time.time())
        aware_dt = timezone.make_aware(naive_dt, ZoneInfo(atz))
        utc_dt_end = aware_dt.astimezone(ZoneInfo("UTC"))
        results = results.filter(
            Q(arrival_date_utc__lt=utc_dt_end.date())
            | (
                Q(arrival_date_utc=utc_dt_end.date())
                & Q(arrival_time_utc__lt=utc_dt_end.time())
            )
        )

    # prices
    if request.GET.get("min_price"):
        results = results.filter(price__gte=request.GET.get("min_price"))
    if request.GET.get("max_price"):
        results = results.filter(price__lte=request.GET.get("max_price"))

    # seats required
    if request.GET.get("seats_required"):
        results = results.filter(seats_available__gte=request.GET.get("seats_required"))

    results = results.order_by("leaving_date_utc", "leaving_time_utc")

    """ CONVERTING DB TIMEZONES FOR DISPLAY """
    for result in results:
        # convert the db's departure times from utc for display
        db_date = result.leaving_date_utc
        db_time = result.leaving_time_utc
        naive_dt = datetime.combine(db_date, db_time)
        aware_dt = timezone.make_aware(naive_dt, ZoneInfo("UTC"))
        if result.direction == "O":
            converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Auckland"))
        elif result.direction == "I":
            if result.route.airport_start.pk == 2:
                converted_dt = aware_dt.astimezone(ZoneInfo("Australia/Sydney"))
            elif result.route.airport_start.pk == 5:
                converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Chatham"))
            else:
                converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Auckland"))
        result.leaving_date_local = converted_dt.date()
        result.leaving_time_local = converted_dt.strftime("%H:%M %Z")

        # convert the db's arrival times from utc for display
        db_date = result.arrival_date_utc
        db_time = result.arrival_time_utc
        naive_dt = datetime.combine(db_date, db_time)
        aware_dt = timezone.make_aware(naive_dt, ZoneInfo("UTC"))
        if result.direction == "I":
            converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Auckland"))
        elif result.direction == "O":
            if result.route.airport_end.pk == 2:
                converted_dt = aware_dt.astimezone(ZoneInfo("Australia/Sydney"))
            elif result.route.airport_end.pk == 5:
                converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Chatham"))
            else:
                converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Auckland"))
        result.arrival_date_local = converted_dt.date()
        result.arrival_time_local = converted_dt.strftime("%H:%M %Z")

    # create page subset of filter results
    paginator = Paginator(results, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    # querystring for when user presses next page button
    qstr_next = request.GET.copy()
    if page.has_next():
        qstr_next["page"] = page.next_page_number()
    qstr_next = "?" + qstr_next.urlencode()

    # querystring for when user presses prev page button
    qstr_prev = request.GET.copy()
    if page.has_previous():
        qstr_prev["page"] = page.previous_page_number()
    qstr_prev = "?" + qstr_prev.urlencode()

    return render(
        request,
        "search.html",
        {
            "form": form,
            "page": page,
            "qstr_next": qstr_next,
            "qstr_prev": qstr_prev,
        },
    )


def addBasket(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if "basket" not in request.session:
        request.session["basket"] = []
    basket = request.session["basket"]
    basket.append({"flight_pk": flight.pk})
    request.session["basket"] = basket

    # subtract item from db
    fm = Flight.objects.get(pk=flight_id)
    fm.seats_available = F("seats_available") - 1
    fm.save()

    return redirect("/search/")


def deleteBasket(request):
    if "basket" not in request.session:
        request.session["basket"] = []
        return redirect("/search/")

    basket = request.session["basket"]

    # add back to db
    for item in basket:
        fm = Flight.objects.get(pk=item["flight_pk"])
        fm.seats_available = F("seats_available") + 1
        fm.save()

    request.session["basket"] = []
    return redirect("/search/")


def booking(request):
    form = BookingForm()

    if "basket" not in request.session:
        request.session["basket"] = []
    basket = request.session["basket"]

    flights = []
    for item in basket:
        flights.append(Flight.objects.get(pk=item["flight_pk"]))

    fflights = []
    for flight in flights:
        fflight = {}
        fflight["unformatted"] = flight

        # if flight is outbound, leaving is pacific/auckland, arriving is whatever
        if flight.direction == "O":

            # departing time conversion
            db_date = flight.leaving_date_utc
            db_time = flight.leaving_time_utc
            db_dt_str = str(db_date) + " " + str(db_time)
            naive_dt = datetime.strptime(db_dt_str, "%Y-%m-%d %H:%M:%S")
            aware_dt = timezone.make_aware(naive_dt, ZoneInfo("UTC"))
            converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Auckland"))
            converted_date = converted_dt.date()
            converted_time = converted_dt.time()
            fflight["depart_date_converted"] = str(converted_date)
            fflight["depart_time_converted"] = str(converted_time) + "+12:00"

            # arrival time conversion
            db_date = flight.arrival_date_utc
            db_time = flight.arrival_time_utc
            db_dt_str = str(db_date) + " " + str(db_time)
            naive_dt = datetime.strptime(db_dt_str, "%Y-%m-%d %H:%M:%S")
            aware_dt = timezone.make_aware(naive_dt, ZoneInfo("UTC"))
            arrival_tz = "UTC"
            arrival_offset = "+00:00"
            if flight.route.airport_end.pk == 2:
                arrival_tz = "Australia/Sydney"
                arrival_offset = "+10:00"
            elif flight.route.airport_end.pk == 5:
                arrival_tz = "Pacific/Chatham"
                arrival_offset = "+12:45"
            else:
                arrival_tz = "Pacific/Auckland"
                arrival_offset = "+12:00"
            converted_dt = aware_dt.astimezone(ZoneInfo(arrival_tz))
            converted_date = converted_dt.date()
            converted_time = converted_dt.time()
            fflight["arrival_date_converted"] = str(converted_date)
            fflight["arrival_time_converted"] = str(converted_time) + arrival_offset

        # if flight is inbound, convert utc to their time
        if flight.direction == "I":

            # departing time conversion
            db_date = flight.leaving_date_utc
            db_time = flight.leaving_time_utc
            db_dt_str = str(db_date) + " " + str(db_time)
            naive_dt = datetime.strptime(db_dt_str, "%Y-%m-%d %H:%M:%S")
            aware_dt = timezone.make_aware(naive_dt, ZoneInfo("UTC"))
            depart_tz = "UTC"
            depart_offset = "+00:00"
            if flight.route.airport_start.pk == 2:
                depart_tz = "Australia/Sydney"
                depart_offset = "+10:00"
            elif flight.route.airport_start.pk == 5:
                depart_tz = "Pacific/Chatham"
                depart_offset = "+12:45"
            else:
                depart_tz = "Pacific/Auckland"
                depart_offset = "+12:00"
            converted_dt = aware_dt.astimezone(ZoneInfo(depart_tz))
            converted_date = converted_dt.date()
            converted_time = converted_dt.time()
            fflight["depart_date_converted"] = str(converted_date)
            fflight["depart_time_converted"] = str(converted_time) + depart_offset

            # arrival time conversion
            db_date = flight.arrival_date_utc
            db_time = flight.arrival_time_utc
            db_dt_str = str(db_date) + " " + str(db_time)
            naive_dt = datetime.strptime(db_dt_str, "%Y-%m-%d %H:%M:%S")
            aware_dt = timezone.make_aware(naive_dt, ZoneInfo("UTC"))
            converted_dt = aware_dt.astimezone(ZoneInfo("Pacific/Auckland"))
            converted_date = converted_dt.date()
            converted_time = converted_dt.time()
            fflight["arrival_date_converted"] = str(converted_date)
            fflight["arrival_time_converted"] = str(converted_time) + "+12:00"

        fflights.append(fflight)

    # calculate total price
    total_price = 0
    for fflight in fflights:
        total_price += fflight["unformatted"].price

    context = {"flights": fflights, "form": form, "total_price": total_price}

    # cast to float because decimal isnt json serializable
    request.session["total_price"] = float(total_price)

    # if post received, validate and process the incoming data
    if request.method == "POST":

        # if there are no flights selected, error
        if len(fflights) == 0:
            context["error_noflights"] = (
                "You have no flights selected to book. Please select flights."
            )
            return render(request, "booking.html", context)

        form = BookingForm(request.POST)
        if form.is_valid():
            cleandata = form.cleaned_data

            # customer code given, try to fetch that customer
            if cleandata.get("customer_code"):
                try:
                    cust = Customer.objects.get(code=cleandata.get("customer_code"))
                except:
                    context["error_customer_code"] = "Customer Not Found"
                    return render(request, "booking.html", context)

            # no customer code given, check the other required fields
            else:
                form_ok = True
                if not cleandata.get("first_name"):
                    form_ok = False
                    context["error_first_name"] = "First Name Required"

                if not cleandata.get("last_name"):
                    form_ok = False
                    context["error_last_name"] = "Last Name Required"

                if not cleandata.get("email"):
                    form_ok = False
                    context["error_email"] = "Email Required"

                if not form_ok:
                    return render(request, "booking.html", context)

                # form is ok, create and add new customer to db
                max_code = Customer.objects.aggregate(Max("code"))
                _code = max_code["code__max"] + 1
                _title = cleandata["title"]
                _first_name = cleandata["first_name"]
                _last_name = cleandata["last_name"]
                _gender = cleandata["gender"]
                _email = cleandata["email"]
                cust = Customer(
                    code=_code,
                    title=_title,
                    first_name=_first_name,
                    last_name=_last_name,
                    gender=_gender,
                    email=_email,
                )
                cust.save()

            # make a new booking using the customer
            _flight_outbound = None
            _flight_outbound_ddate = None
            _flight_outbound_dtime = None
            _flight_outbound_adate = None
            _flight_outbound_atime = None
            _flight_inbound = None
            _flight_inbound_ddate = None
            _flight_inbound_dtime = None
            _flight_inbound_adate = None
            _flight_inbound_atime = None
            for flight in fflights:
                if flight["unformatted"].direction == "O":
                    _flight_outbound = flight["unformatted"]
                    _flight_outbound_ddate = str(flight["depart_date_converted"])
                    _flight_outbound_dtime = str(flight["depart_time_converted"])
                    _flight_outbound_adate = str(flight["arrival_date_converted"])
                    _flight_outbound_atime = str(flight["arrival_time_converted"])
                if flight["unformatted"].direction == "I":
                    _flight_inbound = flight["unformatted"]
                    _flight_inbound_ddate = flight["depart_date_converted"]
                    _flight_inbound_dtime = flight["depart_time_converted"]
                    _flight_inbound_adate = flight["arrival_date_converted"]
                    _flight_inbound_atime = flight["arrival_time_converted"]
            _seats = 1
            _total_price = request.session["total_price"]
            booking = Booking(
                customer=cust,
                flight_outbound=_flight_outbound,
                flight_inbound=_flight_inbound,
                seats=_seats,
                total_price=_total_price,
            )
            booking.save()
            del request.session["basket"]
            context = {
                "booking_id": booking.pk,
                "customer_code": booking.customer.code,
                "customer_first_name": booking.customer.first_name,
                "customer_last_name": booking.customer.last_name,
                "flight_outbound": booking.flight_outbound,
                "flight_outbound_ddate": _flight_outbound_ddate,
                "flight_outbound_dtime": _flight_outbound_dtime,
                "flight_outbound_adate": _flight_outbound_adate,
                "flight_outbound_atime": _flight_outbound_atime,
                "flight_inbound": booking.flight_inbound,
                "flight_inbound_ddate": _flight_inbound_ddate,
                "flight_inbound_dtime": _flight_inbound_dtime,
                "flight_inbound_adate": _flight_inbound_adate,
                "flight_inbound_atime": _flight_inbound_atime,
                "seats": booking.seats,
                "total_price": booking.total_price,
            }
            return render(request, "booking-success.html", context)

    # initial page visit, dont process anything
    else:
        return render(request, "booking.html", context)


def deleteBooking(request):
    if request.method == "POST":
        customer_code = request.POST["customer_code"]
        booking_id = request.POST["booking_id"]

        # if booking_id is associated with customer_id, delete the booking
        try:
            booking = Booking.objects.get(pk=booking_id)
            if str(booking.customer.code) == str(customer_code):

                # outbound flight, return to available flights in db
                outbound_flight = booking.flight_outbound
                if outbound_flight:
                    flight = Flight.objects.get(pk=outbound_flight.pk)
                    flight.seats_available = F("seats_available") + 1
                    flight.save()

                # do the same with inbound flight
                inbound_flight = booking.flight_inbound
                if inbound_flight:
                    flight = Flight.objects.get(pk=inbound_flight.pk)
                    flight.seats_available = F("seats_available") + 1
                    flight.save()

                booking.delete()
                return render(request, "booking-delete-success.html")
        except:
            return render(request, "error.html", {"msg": "Booking Not Found"})

    else:
        form = BookingDeleteForm()
        return render(request, "booking-delete.html", {"form": form})

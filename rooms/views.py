from django_countries import countries
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_agrs = {}
    if city != "Anywhere":
        filter_agrs["city__startswith"] = city

    filter_agrs["country"] = country

    if room_type != 0:
        filter_agrs["room_type__pk"] = room_type

    if price != 0:
        filter_agrs["price__lte"] = price

    if guests != 0:
        filter_agrs["guests__gte"] = guests

    if bedrooms != 0:
        filter_agrs["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_agrs["beds__gte"] = beds

    if baths != 0:
        filter_agrs["baths__gte"] = baths

    if instant is True:
        filter_agrs["instant_book"] = True

    if superhost is True:
        filter_agrs["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_agrs["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_agrs["facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_agrs)

    return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms},)

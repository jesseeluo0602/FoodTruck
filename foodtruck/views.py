from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django import forms
from models import FoodTruck
from .forms import AddressForm
import json
import math
from heapq import heappush, heappop


# Create your views here.
def render_index(request):
	return render(request, 'index.html', {})

# Parse the get request parameters and return the #('num_trucks') closest bird's eye
# distance from the address requested.  Put into heap for slightly faster return
@csrf_exempt
def find_closest(request):
    get_data = request.GET 
    errors = []
    user_lat = get_data.get('latitude', '')
    user_lon = get_data.get('longitude', '')
    num_trucks = get_data.get('num_trucks', 10)
    min_heap = []
    for foodtruck in FoodTruck.objects.all():
        dist_from_address = get_dist((user_lat, user_lon), (foodtruck.latitude, foodtruck.longitude))
        if len(min_heap) < num_trucks:
            heappush(min_heap, (-dist_from_address, foodtruck.id))
        if -dist_from_address > min_heap[0][0]:
            heappop(min_heap)
            heappush(min_heap, (-dist_from_address, foodtruck.id))
    nearest_trucks = []
    for truck_tuple in min_heap:
        nearest_trucks.append(FoodTruck.get_info(truck_tuple[1]))
    response = {
               'status': 200,
               'nearest_trucks': nearest_trucks
              }
    return HttpResponse(json.dumps(response), content_type='application/json')

def get_dist(user_point, foodtruck_point):
    # enums
    LATITUDE = 0
    LONGITUDE = 1
    try:
        return math.sqrt((float(user_point[LATITUDE]) - float(foodtruck_point[LATITUDE]))**2 
            + (float(user_point[LONGITUDE]) - float(foodtruck_point[LONGITUDE]))**2)
    except ValueError:
        return float("inf")

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
def index(request):
	food_truck_info = FoodTruck.objects
	return render(request, 'index.html', {})

@csrf_exempt
def find_closest(request):
    # assert request.method == 'POST', 'api/find_closest/ has to be a POST request'
    errors = []
    post = QueryDict('', mutable=True)
    post.update(json.loads(request.body))
    user_lat = post.get('latitude', '')
    user_lon = post.get('longitude', '')
    min_heap = []
    test = []
    for foodtruck in FoodTruck.objects.all():
        dist_from_address = get_dist((user_lat, user_lon), (foodtruck.latitude, foodtruck.longitude))
        test.append(dist_from_address)
        if len(min_heap) < 10:
            print foodtruck.truck_name
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

def get_address(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddressForm()

    return render(request, 'index.html', {'form': form})
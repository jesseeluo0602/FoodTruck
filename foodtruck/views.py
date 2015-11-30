from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import FoodTruck
import json



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
    nearest_trucks = FoodTruck.get_closest(user_lat, user_lon, num_trucks)
    response = {
               'status': 200,
               'nearest_trucks': nearest_trucks
              }
    return HttpResponse(json.dumps(response), content_type='application/json')



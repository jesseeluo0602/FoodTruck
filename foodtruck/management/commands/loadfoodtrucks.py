from django.core.management.base import BaseCommand, CommandError
from foodtruck.models import FoodTruck
import json
import urllib2
from heapq import heappush, heappop
import math


# This Command is used to load the food truck data into your database.  Run 
# python manage.py loadfoodtrucks <filename>
# also, using "web" as file name will default to making a get request to 
# th DataSF food truck doc: 'https://data.sfgov.org/resource/rqzj-sfat.json'
class Command(BaseCommand):
    help = 'Loads food truck data into db'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    # delete the databse if it exists, the insert rows afterwards.
    def handle(self, *args, **options):
        try:
            FoodTruck.objects.all().delete()
            filename = options['filename'][0]
            if filename == 'web':
                json_data = json.loads(urllib2.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json').read())
            else:
                json_data = json.loads(open(filename).read())
            for table_row in json_data:
                truck_name = address = latitude = longitude = schedule_url = operation_hours = food_items= ""
                if 'applicant' in table_row:
                    truck_name = table_row['applicant']
                if 'address' in table_row:
                    address = table_row['address']
                if 'latitude' in table_row:
                    latitude = table_row['latitude']
                if 'longitude' in table_row:
                    longitude = table_row['longitude']
                if 'schedule' in table_row:
                    schedule_url = table_row['schedule']
                if 'dayshours' in table_row:
                    operation_hours = table_row['dayshours']
                if 'fooditems' in table_row:
                    food_items = table_row['fooditems']
                # make sure there are no duplicate entries inside our database
                if not FoodTruck.objects.filter(truck_name=truck_name, latitude=latitude, longitude=longitude).exists():
                    new_food_truck = FoodTruck(truck_name=truck_name, address=address, latitude=latitude, 
                        longitude=longitude, schedule_url=schedule_url, operation_hours=operation_hours, 
                        food_items=food_items)
                    new_food_truck.save()
        except Exception as e:
            print e

    def get_dist(self, user_point, foodtruck_point):
        # enums
        LATITUDE = 0
        LONGITUDE = 1
        try:
            return math.sqrt((user_point[LATITUDE] - float(foodtruck_point[LATITUDE]))**2 
                + (user_point[LONGITUDE] - float(foodtruck_point[LONGITUDE]))**2)
        except ValueError:
            return float("inf")




        

from django.core.management.base import BaseCommand, CommandError
from foodtruck.models import FoodTruck
import json
import urllib2
from heapq import heappush, heappop
import math

class Command(BaseCommand):
    help = 'Loads food truck data into db'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            FoodTruck.objects.all().delete()
            filename = options['filename'][0]
            if filename == 'web':
                json_data = json.loads(urllib2.urlopen('https://data.sfgov.org/resource/rqzj-sfat.json').read())
            else:
                json_data = json.loads(open(filename).read())
            for table_row in json_data:
                truck_name = address = latitude = longitude = schedule_url = operation_hours = ""
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
                new_food_truck = FoodTruck(truck_name=truck_name, address=address, latitude=latitude, 
                    longitude=longitude, schedule_url=schedule_url, operation_hours=operation_hours)
                new_food_truck.save()
            user_lat = 37
            user_lon = 122
            min_heap = []
            test = []
            for foodtruck in FoodTruck.objects.all():
                dist_from_address = self.get_dist((user_lat, user_lon), (foodtruck.latitude, foodtruck.longitude))
                test.append(dist_from_address)
                if len(min_heap) < 10:
                    print foodtruck.truck_name
                    heappush(min_heap, (-dist_from_address, foodtruck.id))
                # print -dist_from_address > min_heap[0], -dist_from_address, min_heap[0]
                if -dist_from_address > min_heap[0][0]:
                    # print "hello"
                    heappop(min_heap)
                    heappush(min_heap, (-dist_from_address, foodtruck.id))
            print sorted(min_heap, reverse=True)
            test = sorted(test)
            print test[:10]
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




        

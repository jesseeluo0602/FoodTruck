from django.db import models
import math
from heapq import heappush, heappop

# Create your models here.
class FoodTruck(models.Model):
    truck_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    schedule_url = models.CharField(max_length=200)
    operation_hours = models.CharField(max_length=200)
    food_items = models.CharField(max_length=500)

    class Meta:
        unique_together = ('truck_name', 'latitude', 'longitude')

    def __str__(self):              # __unicode__ on Python 2
       return self.truck_name

    def get_info(self):
        foodtruck_dict = {
            "truck_name": self.truck_name,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "schedule_url": self.schedule_url,
            "operation_hours": self.operation_hours,
            "food_items": self.food_items,
        }
        return foodtruck_dict

    @staticmethod
    def get_closest(user_lat, user_lon, num_trucks):
        min_heap = []
        for foodtruck in FoodTruck.objects.all():
            dist_from_address = FoodTruck.get_dist((user_lat, user_lon), (foodtruck.latitude, foodtruck.longitude))
            if len(min_heap) < num_trucks:
                heappush(min_heap, (-dist_from_address, foodtruck))
            if -dist_from_address > min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (-dist_from_address, foodtruck))
        nearest_trucks = []
        for truck_tuple in min_heap:
            nearest_trucks.append(truck_tuple[1].get_info())
        return nearest_trucks

    @staticmethod
    def get_dist(user_point, foodtruck_point):
        # enums
        LATITUDE = 0
        LONGITUDE = 1
        try:
            return math.sqrt((float(user_point[LATITUDE]) - float(foodtruck_point[LATITUDE]))**2 
                + (float(user_point[LONGITUDE]) - float(foodtruck_point[LONGITUDE]))**2)
        except ValueError:
            return float("inf")

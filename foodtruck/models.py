from django.db import models

# Create your models here.
class FoodTruck(models.Model):
    truck_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    schedule_url = models.CharField(max_length=200)
    operation_hours = models.CharField(max_length=200)

    class Meta:
        unique_together = ('truck_name', 'latitude', 'longitude')

    def __str__(self):              # __unicode__ on Python 2
       return self.truck_name

    @staticmethod
    def get_info(truck_id):
        if FoodTruck.objects.filter(id=truck_id).exists():
	        foodtruck = FoodTruck.objects.get(id=truck_id)
	        foodtruck_dict = {
		        "truck_name": foodtruck.truck_name,
		        "address": foodtruck.address,
		        "latitude": foodtruck.latitude,
		        "longitude": foodtruck.longitude,
		        "schedule_url": foodtruck.schedule_url,
		        "operation_hours": foodtruck.operation_hours,
	        }
        	return foodtruck_dict
        return {}
    


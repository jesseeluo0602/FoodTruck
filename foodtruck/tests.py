from django.test import TestCase
from models import FoodTruck

# Create your tests here.
class FoodTruckTestCase(TestCase):

	def setUp(self):
		FoodTruck.objects.create(truck_name="truck1", address="address1", latitude="5", 
			longitude="5", schedule_url="schedule1", operation_hours="hours1", food_items="food_items")
		FoodTruck.objects.create(truck_name="truck2", address="address2", latitude="world", 
			longitude="hello", schedule_url="schedule2", operation_hours="hours2", food_items="food_items")
		FoodTruck.objects.create(truck_name="truck3", address="address3", latitude="8", 
			longitude="8", schedule_url="schedule3", operation_hours="hours3", food_items="food_items")
		FoodTruck.objects.create(truck_name="truck4", address="address4", latitude="9", 
			longitude="9", schedule_url="schedule4", operation_hours="hours4", food_items="food_items")
		FoodTruck.objects.create(truck_name="truck5", address="address5", latitude="10", 
			longitude="10", schedule_url="schedule5", operation_hours="hours5", food_items="food_items")

	def test_get_info(self):
		truck1 = FoodTruck.objects.get(truck_name="truck1")
		self.assertEqual(truck1.get_info(), {'truck_name':"truck1", 'address':"address1", 'latitude':"5", 
			'longitude':"5", 'schedule_url':"schedule1", 'operation_hours':"hours1", 'food_items':"food_items"})

	def test_get_dist(self):
		point1 = (0,0)
		point2 = (2,0)
		# basic test
		self.assertEqual(FoodTruck.get_dist(point1, point2), 2)

		# make sure it works, tested with wolfram alpha
		point2= (37.111, 120.55)
		self.assertEqual(FoodTruck.get_dist(point1, point2), 126.13298070290736)

	def test_get_closest(self):
		truck1 = FoodTruck.objects.get(truck_name="truck1")
		truck2 = FoodTruck.objects.get(truck_name="truck2")
		truck3 = FoodTruck.objects.get(truck_name="truck3")
		truck4 = FoodTruck.objects.get(truck_name="truck4")
		truck5 = FoodTruck.objects.get(truck_name="truck5")

		# results closest to origin should be truck 1 and truck 3, it should ignore truck 2 because it 
		# does not have sane long/lat values 
		result = FoodTruck.get_closest(0, 0, 2)
		self.assertIn(truck1.get_info(), result)
		self.assertIn(truck3.get_info(), result)
		self.assertNotIn(truck2.get_info(), result)
		self.assertNotIn(truck4.get_info(), result)
		self.assertNotIn(truck5.get_info(), result)


		result = FoodTruck.get_closest(100, 100, 2)
		self.assertIn(truck4.get_info(), result)
		self.assertIn(truck5.get_info(), result)
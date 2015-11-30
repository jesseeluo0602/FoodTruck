# FoodTruckFinder


# Overview
Web app written with Django and AngularJS that allows users to find the nearest food trucks near them.  A user can either
enter in an address in the autocomplete or click on the map in order to populate the results and put markers on the map.

# Running this app
Make sure you have pip installed
pip install -r requirements.txt

git clone https://github.com/jesseeluo0602/FoodTruck.git
python manage.py syncdb
python manage.py loadfoodtrucks web     -- web is the default json found at https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat
You can replace web with a json file and will still work as long as it has the same headers. Django command can be found in foodtruck/management/commands
python manage.py runserver

# Testing
Unit tests for python are found in foodtruck/tests.py
python manage.py tests

Frontend Jasmine Tests - TODO: need to change from regualr google maps to angular-maps.  Currently frontend tests can't compile corectly because the google map is not loaded correctly.
Make sure nodeJS is installed
npm install
npm test

# Comments
Had no Django experience previous to this and have self-taught angular experience (with a bit of guidance at my last internship but no real "angular" guru to guide me or correct me).
Thought building the app was a great learning experience and would appreciate any feedback and reviews so that I can learn from my mistsakes and improve next time!

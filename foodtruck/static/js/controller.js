(function() {
  'use strict';

  angular
    .module('FoodTruck', [])
    .controller('IndexController', IndexController)
    // distinction between angular brackets and django templating brackets
    .config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('[[');
      $interpolateProvider.endSymbol(']]');
    });

  function IndexController($http) {

    // vm.query: parameters for the get request, {latitude, longitude, address }
    // vm.results: list of closest food trucks returned in the get response
    // vm.markers: list of google map markers that are currently on the map
    // vm.clickedQuery: whether or not it was a form submission or a map-click
    var vm = this;
    vm.query = {};
    vm.results = [];
    vm.markers = [];
    vm.clickedQuery = false;

    // http get call to our backend that will return the list of 10 closest food trucks
    vm.findClosest = function() {
      if (vm.query != {}) {
        $http.get("/api/find_closest", {
          params: vm.query
        }).then(
          function successCallBack(response) {
            var data = response.data;
            vm.results = data.nearest_trucks;
            if (vm.results.length > 0) {
              vm.deleteMarkers();
              vm.markers = [];
              vm.addMarkers();
            }
          })
      }
    }

    // when a query is submitted through the address form, when something is clicked it goes through the listener
    vm.submitQuery = function() {
      vm.clickedQuery = false;
      var place = vm.autocomplete.getPlace();
      vm.query.longitude = place.geometry.location.lng();
      vm.query.latitude = place.geometry.location.lat();
      vm.query.address = place.formatted_address;
      if (vm.query != {}) {
        vm.findClosest(vm.query);
      }
    }

    // GOOGLE MAPS SECTION

    // Marker functions
    // Add one marker on map
    vm.addMarker = function(foodtruck, index) {
      var infoWindow = new google.maps.InfoWindow();
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(foodtruck.latitude, foodtruck.longitude),
        map: vm.map,
        animation: google.maps.Animation.DROP,
        label: index.toString(),
        title: foodtruck.truck_name,
      });
      // Add listener to open small content box
      google.maps.event.addListener(marker, 'click', function() {
        infoWindow.setContent('<h3>' + marker.title + '</h3>');
        infoWindow.open(vm.map, marker);
      });
      vm.markers.push(marker);
    }

    // Add markers for results on map
    vm.addMarkers = function() {
      for (var i = 0; i < vm.results.length; i++) {
        vm.addMarker(vm.results[i], i + 1);
      }
    }

    // Delete all markers from map
    vm.deleteMarkers = function() {
      for (var i = 0; i < vm.markers.length; i++) {
        var marker = vm.markers[i];
        marker.setMap(null);
      }
    }

    // Initialize google maps
    // Set center of map to San Francisco and give it an initial zoom magnitude
    var mapOptions = {
      center: {
        lat: 37.7749295,
        lng: -122.41941550000001
      },
      scrollwheel: false,
      zoom: 12,
    }

    vm.map = new google.maps.Map(document.getElementById('map'), mapOptions);
    // Create the autocomplete object, restricting the search to geographical
    // location types.
    vm.autocomplete = new google.maps.places.Autocomplete(
      (document.getElementById('autocomplete')), {
        types: ['geocode']
      });

    google.maps.event.addListener(vm.map, 'click', function(event) {
      // addMarker(event.latLng, map);
      vm.query.latitude = event.latLng.lat();
      vm.query.longitude = event.latLng.lng();
      vm.clickedQuery = true;
      vm.findClosest();
    });


    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var geolocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        var circle = new google.maps.Circle({
          center: geolocation,
          radius: position.coords.accuracy
        });
        vm.autocomplete.setBounds(circle.getBounds());
      });
    }

  };
})();

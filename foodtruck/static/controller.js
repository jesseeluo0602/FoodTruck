var app = angular.module('LocalCart', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

app.controller('IndexController', function($http, $window) {
  var vm = this;
  vm.query = {}
  vm.results = []
  vm.find_closest = function() {
    console.log(autocomplete.getPlace())
    var place = autocomplete.getPlace();
    vm.query.longitude = place.geometry.location.lng();
    vm.query.latitude = place.geometry.location.lat();
    vm.query.address = place.formatted_address
    console.log(vm.query);
    if (vm.query != {}) {
      $http.post("/api/find_closest", vm.query).then(
        function successCallBack(response) {
          var data = response.data;
          vm.results = data.nearest_trucks
          if (vm.results.length > 0) {
            vm.deleteMarkers();
            vm.markers = [];
            vm.addMarkers();
          }
        })
    }
    console.log(vm.markers);

  }


  vm.markers = []

  vm.addMarker = function(foodtruck, index) {
    console.log(index);
    var marker = new google.maps.Marker({
      position: new google.maps.LatLng(foodtruck.latitude, foodtruck.longitude),
      map: vm.map,
      animation: google.maps.Animation.DROP,
      label: index.toString(),
    });
    vm.markers.push(marker);
    console.log(vm.markers);
  }

  vm.addMarkers = function() {
    for (var i = 0; i < vm.results.length; i++) {
      vm.addMarker(vm.results[i], i);
    }
  }

  vm.deleteMarkers = function() {
    console.log(vm.markers);
    for (var i = 0; i < vm.markers.length; i++) {
      var marker = vm.markers[i]
      marker.setMap(null);
    }  
  }

  var mapOptions = {
    center: {
      lat: 37.7749295,
      lng: -122.41941550000001
    },
    scrollwheel: false,
    zoom: 12
  }

  vm.map = new google.maps.Map(document.getElementById('map'), mapOptions);
  // Create the autocomplete object, restricting the search to geographical
  // location types.
  autocomplete = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */
    (document.getElementById('autocomplete')), {
      types: ['geocode']
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
      autocomplete.setBounds(circle.getBounds());
    });
  }


});

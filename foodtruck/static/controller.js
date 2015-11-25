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
    $http.post("/api/find_closest", vm.query).then(
        function successCallBack(response) {
          var data = response.data;
          vm.results = data.nearest_trucks
        })
  }


    var mapOptions = {
      center: {
        lat: 37.7749295,
        lng: -122.41941550000001
      },
      scrollwheel: false,
      zoom: 12
    }

    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
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

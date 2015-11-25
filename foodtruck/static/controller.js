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
    $http.post("/api/find_closest", vm.query).then(
        function successCallBack(response) {
          var data = response.data;
          vm.results = data.nearest_trucks
        })
  }
});

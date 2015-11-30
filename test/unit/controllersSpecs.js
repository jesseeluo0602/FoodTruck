'use strict';

// testing controller
describe('IndxController', function() {
   var $httpBackend, $rootScope, createController, authRequestHandler;

   // Set up the module
   beforeEach(module('FoodTruck'));

   beforeEach(inject(function($injector) {
     // Set up the mock http service responses
     $httpBackend = $injector.get('$httpBackend');
     // backend definition common for all tests
     authRequestHandler = $httpBackend.when('GET', '/api/find_closest')
      .respond({"status": 200, "nearest_trucks": [{"schedule_url": "http://fakesite.com/schedule.pdf", "food_items": "sandwiches", "operation_hours": "Mo/Mo/Mo/Mo/Mo:7AM-8AM/9AM-11AM;", "truck_name": "Truck1", "latitude": "37.7721522432444", "longitude": "-122.387742984116", "address": "FakeAddress 1"}]});
   

     // Get hold of a scope (i.e. the root scope)
     $rootScope = $injector.get('$rootScope');
     // The $controller service is used to create instances of controllers
     var $controller = $injector.get('$controller');

     createController = function() {
       return $controller('IndexController', {'$scope' : $rootScope });
     };
   }));

  // unit testing

  it('should create results and markers model with 1 food truck', function() {
    $httpBackend.expectGET('/api/find_closest');
    var controller = createController();
    $httpBackend.flush();

    expect(scope.results).toEqualData([]);
    expect(scope.markers).toEqualData([]);
    $httpBackend.flush();

    expect(scope.results).toEqualData(
        [{"schedule_url": "http://fakesite.com/schedule.pdf", "food_items": "sandwiches", "operation_hours": "Mo/Mo/Mo/Mo/Mo:7AM-8AM/9AM-11AM;", "truck_name": "Truck1", "latitude": "37.7721522432444", "longitude": "-122.387742984116", "address": "FakeAddress 1"}]);
    
    expect(scope.markers.length).toEqualData(1);


    it('should set the default value of clickedQuery model', function() {
      expect(scope.clickedQuery).toBe(false);
    });


    it('should set the default value of query model', function() {
      expect(scope.query).toBe({});
    });
  });

});
'use strict';

/* jasmine specs for controllers go here */
describe('FoodTruck controller', function() {

  beforeEach(module('FoodTruck'));

  describe('IndexController', function(){
    var scope, ctrl, $httpBackend;

    beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
      $httpBackend = _$httpBackend_;
      $httpBackend.expectGET('/api/find_closest').
        respond({"status": 200, "nearest_trucks": [{"schedule_url": "http://fakesite.com/schedule.pdf", "food_items": "sandwiches", "operation_hours": "Mo/Mo/Mo/Mo/Mo:7AM-8AM/9AM-11AM;", "truck_name": "Truck1", "latitude": "37.7721522432444", "longitude": "-122.387742984116", "address": "FakeAddress 1"}]})
      scope = $rootScope.$new();
      ctrl = $controller('IndexController', {$scope: scope});
    }));

    it('should create results and markers model with 1 food truck', function() {
      expect(scope.results).toEqualData([]);
      expect(scope.markers).toEqualData([]);
      $httpBackend.flush();

      expect(scope.results).toEqualData(
          [{"schedule_url": "http://fakesite.com/schedule.pdf", "food_items": "sandwiches", "operation_hours": "Mo/Mo/Mo/Mo/Mo:7AM-8AM/9AM-11AM;", "truck_name": "Truck1", "latitude": "37.7721522432444", "longitude": "-122.387742984116", "address": "FakeAddress 1"}]);
      
      expect(scope.markers.length).toEqualData(1);
    });

    it('should set the default value of clickedQuery model', function() {
      expect(scope.clickedQuery).toBe(false);
    });

    it('should set the default value of query model', function() {
      expect(scope.query).toBe({});
    });

  });
});
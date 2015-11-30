module.exports = function(config){
  config.set({

    basePath : '../',

    files : [
      "https://code.jquery.com/jquery-2.1.4.min.js",
      "https://maps.googleapis.com/maps/api/js?key=AIzaSyD-eJHV0gRr7b1h4X0i1605Rpf6flWXD6A&signed_in=true&libraries=places",
      "https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js",
      "https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular-mocks.js",
      'foodtruck/static/*.js',
      'test/unit/**/*.js',
    ],

    autoWatch : true,

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
            'karma-chrome-launcher',
            'karma-jasmine'
            ],

    junitReporter : {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    }

  });
};
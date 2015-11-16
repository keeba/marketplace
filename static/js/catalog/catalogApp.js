angular.module('catalogApp', [
  'ui.router',
  'ngResource',
  'catalogApp.services',
  'catalogApp.controllers'		
])
  .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;

    // Django expects jQuery like headers
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    // Routing

    $urlRouterProvider.otherwise('/products');
    $stateProvider
      .state('catalog', {
        url: '/catalog',
        templateUrl: '/static/js/catalog/catalog.html',
        controller: 'CatalogCtrl',
      })
      .state('products', {
        url: '/products',
        templateUrl: '/static/js/catalog/products.html',
        controller: 'ProductCtrl',
      })
      .state('newcatalog', {
        url: '/catalog',
        templateUrl: '/static/js/catalog/add_catalog.html',
        controller: 'CatalogCtrl',
      })
      .state('editcatalog', {
        url: '/catalog/:catalogId',
        templateUrl: '/static/js/catalog/add_catalog.html',
        controller: 'CatalogCtrl',
      })
      .state('newproduct', {
        url: '/products',
        templateUrl: '/static/js/catalog/add_product.html',
        controller: 'ProductCtrl',
      })
      .state('editproduct', {
        url: '/products/:productId',
        templateUrl: '/static/js/catalog/add_product.html',
        controller: 'ProductCtrl',
      })
      .state('viewproduct', {
        url: '/products/view/:productId',
        templateUrl: '/static/js/catalog/view_product.html',
        controller: 'ProductCtrl',
      })
  });

var catalogControllers = angular.module('catalogApp.controllers', []);

catalogControllers.controller('ProductCtrl',['$scope','$stateParams','$state','Product','Category','SubCategory','AuthUser',
'$window',function ProductCtrl($scope,$stateParams,$state,Product,Category,SubCategory,AuthUser,$window) {
	$scope.products_tab_active=1;
	$scope.authuser = AuthUser;
    if("productId" in $stateParams) 	
    {
    	$scope.product = {};
		$id = $stateParams.productId;
    	$scope.product = Product.get( { id: $id }); 
    }
	else
	{
		$scope.products = [];	
		Product.query(function(response) {
			$scope.products = response;
		});
	}
	Category.query(function(response) {
		$scope.categories = response;
	});
	SubCategory.query(function(response) {
		$scope.subcategories = response;
	});
    $scope.saveProduct = function(product) {
		if("productId" in $stateParams) 
		{	
  			Product.update({id: $stateParams.productId},product);		
		}
		else
		{
  			Product.save(product);	
		} 
		$state.go('products');  
    }
    $scope.deleteProduct = function(product) {
  	  if($window.confirm('Are you sure?'))
  	  {		
  		  if(Product.delete(product))
  		  {
  			  var index = $scope.products.indexOf(product);
  			  $scope.products.splice(index, 1);
  		  }
  	  }
    }
}]);

catalogControllers.controller('CatalogCtrl',['$scope','$stateParams','$state','Catalog','Category','SubCategory','AuthUser','Product','$window',
	  function CatalogCtrl($scope,$stateParams,$state,Catalog,Category,SubCategory,AuthUser,Product,$window) {
	$scope.catalog_tab_active=1;		  
	$scope.authuser = AuthUser;
    if("catalogId" in $stateParams) 	
    {
    	$scope.catalog = {};
		$id = $stateParams.catalogId;
    	$scope.catalog = Catalog.get( { id: $id }); 
    }
	else
	{
		$scope.catalogs = [];	
		Catalog.query(function(response) {
			$scope.catalogs = response;
		});			
	}
	Product.query(function(response) {
		$scope.products = response;
	});
	Category.query(function(response) {
		$scope.categories = response;
	});
	SubCategory.query(function(response) {
		$scope.subcategories = response;
	});
    $scope.saveCatalog = function(catalog) {
		if("catalogId" in $stateParams) 
		{	
  			Catalog.update({id: $stateParams.catalogId},catalog);		
		}
		else
		{
  			Catalog.save(catalog);	
		} 
		$state.go('catalog');  
    }
    $scope.deleteCatalog = function(catalog) {
  	  if($window.confirm('Are you sure?'))
  	  {		
  		  if(Catalog.delete(catalog))
  		  {
  			  var index = $scope.catalogs.indexOf(catalog);
  			  $scope.catalogs.splice(index, 1);
  		  }
  	  }
    }
}]);

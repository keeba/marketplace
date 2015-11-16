// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('catalogApp.services', ['ngResource'])
  .factory('Product', function($resource) {
	  return $resource('/api/products/:id/',null,{'update': { method:'PUT' }});
  })
  .factory('Catalog', function($resource) {
	  return $resource('/api/catalog/:id/',null,{'update': { method:'PUT' }}); 
  })
  .factory('Category', function($resource) {
	  return $resource('/api/categories/:id/'); 	  
  })
  .factory('SubCategory', function($resource) {
	  return $resource('/api/subcategories/:id/'); 	  
  });

 


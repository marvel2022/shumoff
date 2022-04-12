console.log("Hello World")

function cart_detail_view($this){
	var productPk = $this.dataset.product;
	var action = $this.dataset.action;
	var pageId = $this.dataset.id;
	var price_option_pk = $this.dataset.optionpk
	var order_quantity = 1
	if (pageId == "cart-page"){
	  console.log("cart-page")
	} else {
	  price_option_pk = document.getElementById("ProductPriceHidden").innerHTML;
	  order_quantity = document.getElementById("OrderQuantity").value; 
	}
	console.log('productPk: ', productPk, 'Action:', action);
	console.log('USER: ', user);
	console.log('USER: ', user);
	console.log('order_quantity: ', order_quantity)
	
	console.log('price_option_pk: ', price_option_pk);
  
	if (user == 'AnonymousUser'){
	  LoginSignUpFunction(productPk)
	  console.log("User is not logged in")
	}else{
	  console.log("User is logged in")
	  updateUserOrder(productPk, action, pageId, price_option_pk, order_quantity)
	}  
  }
  
  function updateUserOrder(productPk, action, pageId, price_option_pk, order_quantity){
	console.log('User is authenticated, sending data...')
  
	var url = '/ajax/cart/detail/'
  
	fetch(url, {
	  method:'POST',
	  headers:{
		'Content-Type':'application/json',
		'Accept': 'application/json',
		'X-CSRFToken':csrftoken,
	  }, 
	  body:JSON.stringify({'productPk':productPk, 'action':action, 'pageId':pageId, 'price_option_pk': price_option_pk, 'order_quantity':order_quantity})
	})
	.then((response) => {
	   return response.json();
	})
	.then((data) => {
	  var notif_tag = document.getElementById('AlreadyAdded'+productPk.toString());
	
	  if(pageId == "cart-page"){
		location.reload()
	  }
	  if (notif_tag != null){
		if (data["added"] == true && pageId == "product-page"){
			notif_tag.innerHTML = 'Добавлено в корзину';
			notif_tag.classList.toggle("show");
		}
		if (data["already_added"] == true && pageId == "product-page"){
			notif_tag.innerHTML = 'Уже выбрано';
			notif_tag.classList.toggle("show");
		}
		if (data["less_then"] == true){
			notif_tag.innerHTML = 'доступный продукт - '+data["available_quanity"].toString();
			notif_tag.classList.toggle("show");
		}
	  }
	});
  }
  
  // When the user clicks on div, open the popup
  function LoginSignUpFunction(productPk) {
		console.log("This method works fine")
		var popup = document.getElementById("PopupNotification"+productPk.toString());
		popup.classList.toggle("show");
	}
  
  
  function product_price($this){
	var price = $this.dataset.price;
	var price_info = $this.dataset.priceinfo;
	var pk = $this.dataset.pk;
	var discount = $this.dataset.discount
  
	var display_price = document.getElementById("ProductPrice");
	var display_price_info = document.getElementById("ProductPriceInfo");
	var price_option = document.getElementById("ProductPriceHidden");

	if (discount == 'discount'){
		display_price.innerHTML = price;
		display_price_info.innerHTML = price_info;
		price_option.innerHTML = pk
	  }else{
		display_price.innerHTML = "<small><del>"+discount.toString()+"</del>"+price_info.toString()+"</small><br>"+price.toString();
		display_price_info.innerHTML = price_info;
		price_option.innerHTML = pk
	  }
	
	  console.log(price, price_info, pk);
	}


// function cart_detail_view($this){
// 	var productPk = $this.dataset.product;
// 	var action = $this.dataset.action;
// 	var pageId = $this.dataset.id;
// 	var price_option_pk = $this.dataset.optionpk
// 	var 
// 	if (pageId == "cart-page"){
// 		console.log("cart-page")
		// -> var price_option_pk = document.getElementById("ProductPriceHidden"+productPk.toString()).innerHTML;
// 	} else {
// 		var price_option_pk = document.getElementById("ProductPriceHidden").innerHTML;
// 	}
// 	console.log('productPk: ', productPk, 'Action:', action);
// 	console.log('USER: ', user);
// 	console.log('USER: ', user);
	
// 	console.log('price_option_pk: ', price_option_pk);

// 	if (user == 'AnonymousUser'){
// 		LoginSignUpFunction(productPk)
// 		console.log("User is not logged in")
// 	}else{
// 		console.log("User is logged in")
// 		updateUserOrder(productPk, action, pageId, price_option_pk)
// 	}	
// }

// function updateUserOrder(productPk, action, pageId, price_option_pk){
// 	console.log('User is authenticated, sending data...')

// 	var url = '/ajax/cart/detail/'

// 	fetch(url, {
// 		method:'POST',
// 		headers:{
// 			'Content-Type':'application/json',
// 			'Accept': 'application/json',
// 			'X-CSRFToken':csrftoken,
// 		}, 
// 		body:JSON.stringify({'productPk':productPk, 'action':action, 'pageId':pageId, 'price_option_pk': price_option_pk})
// 	})
// 	.then((response) => {
// 	   return response.json();
// 	})
// 	.then((data) => {
// 		var notif_tag = document.getElementById('AlreadyAdded'+productPk.toString());
	
// 		if(pageId == "cart-page"){
// 			location.reload()
// 		}
		// -> location.reload()
		// console.log(data["done_action"])
		// -> {"added":False, "removed":False, "cleared":False, "new_added":False}
		// if (notif_tag != null){
		// 	if (data["added"] == true && pageId == "product-page"){
				// -> alert("New product added to your cart.")
				// -> notif_tag.innerHTML = 'Добавлено в корзину';
				// notif_tag.classList.toggle("show");
				// -> $('#AlreadyAdded'+productPk.toString()).hide(5000);
				// -> added_to_cart()
			// }
			// if (data["already_added"] == true && pageId == "product-page"){
				// -> alert("This product was already added to your cart.")
				// notif_tag.innerHTML = 'Уже выбрано';
				// notif_tag.classList.toggle("show");
				// -> $('#AlreadyAdded'+productPk.toString()).hide(5000);
// 			}
// 		}
// 	});
// }

// -> When the user clicks on div, open the popup
// function LoginSignUpFunction(productPk) {
// 	console.log("This method works fine")
// 	var popup = document.getElementById("PopupNotification"+productPk.toString());
// 	popup.classList.toggle("show");
	// -> $('#PopupNotification'+productPk.toString()).hide(5000);
//   }

// ---->
// $(".add-to-basket").on('click', function () {
// 	$('#AlreadyAdded'+productPk.toString()).hide(500);
// 	console.log('#AlreadyAdded'+productPk.toString());
// });
  

// (function(){
// 	$('.add-to-basket').on('click', function(e){
// 	  e.preventDefault();
// 	  $.notify('Продукт был добавлен в корзину.', 'success','5000','top');
// 	});
  
//   })(jQuery);

// function added_to_cart(){
// 	// e.preventDefault();
// 	$.notify('Продукт был добавлен в корзину.', 'success','5000','top');
// }
// ---->

// function product_price($this){
// 	var price = $this.dataset.price;
// 	var price_info = $this.dataset.priceinfo;
// 	var pk = $this.dataset.pk;
// 	var display_price = document.getElementById("ProductPrice");
// 	var display_price_info = document.getElementById("ProductPriceInfo");
// 	var price_option = document.getElementById("ProductPriceHidden");
// 	display_price.innerHTML = price;
// 	display_price_info.innerHTML = price_info;
// 	price_option.innerHTML = pk

// 	console.log(price, price_info, pk);
// }



$('#recipeCarousel').carousel({
  interval: 1000
});

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 3;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));
    
    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
          next = $(this).siblings(':first');
        }
        
        next.children(':first-child').clone().appendTo($(this));
      }
});







window.replainSettings = { id: '3620ea29-af84-4de5-b94e-8b4fd4f6a378' };
(function(u){var s=document.createElement('script');s.type='text/javascript';s.async=true;s.src=u;
var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);

// x=document.getElementsByTagName('script').style.color = "blue";

})('https://widget.replain.cc/dist/client.js');




  $(document).ready(function(){

    $.fakeLoader({
      timeToHide:1000,
      bgColor:"#ff780f",
      // spinner:"spinner1",
      //spinner:"spinner2",
      // spinner:"spinner3",
      // spinner:"spinner4",
      //spinner:"spinner5",
      //spinner:"spinner6",
      spinner:"spinner7",
      // imagePath:"../img/logo.png",
    });
  });


  // Crol to top
  var $btnTop = $(".btn-top");
  $(window).on("scroll",function(){
    if($(window).scrollTop() >= 20)
    {
      $btnTop.fadeIn();
    }
    else{
      $btnTop.fadeOut();
    }
  });
  $btnTop.on("click",function(){
    $("html,body").animate({scrollTop:0},1200)
  });




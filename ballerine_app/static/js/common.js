/**
 * Created by GeneralKenobi on 07.11.2016.
 */


$(document).ready(function() {
  $('.popup_image').magnificPopup(
      {
          type: 'image',
		closeOnContentClick: true,
		closeBtnInside: false,
		fixedContentPos: true,
		image: {
			verticalFit: true
		},
		zoom: {
			enabled: true,
			duration: 300 // don't foget to change the duration also in CSS
		}
      }
  );
});


var $document = $(document),
    $element = $('.head'),
    className = 'nav-scrolled';

$document.scroll(function() {
  scrollTop = $document.scrollTop()
  if (scrollTop > 50) {
    // user scrolled 50 pixels or more;
    // do stuff
    $element.addClass(className);
  } else {
    $element.removeClass(className);
  }

  if(scrollTop < 700){
    $('.first_section').css({
      backgroundPosition: 'center ' +  scrollTop*0.2 + 'px'
    })
  }
});

$('.mouse-wheel').click(function () {
  $('html, body').stop().animate({
    scrollTop: $(".second_section").offset().top
  }, 1000);
})

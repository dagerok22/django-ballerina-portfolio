/**
 * Created by GeneralKenobi on 07.11.2016.
 */



var $document = $(document),
    $element = $('.head'),
    className = 'nav-scrolled';

$document.scroll(function() {
  if ($document.scrollTop() > 50) {
    // user scrolled 50 pixels or more;
    // do stuff
    $element.addClass(className);
  } else {
    $element.removeClass(className);
  }
});

$('.mouse-wheel').click(function () {
  $('html, body').stop().animate({
    scrollTop: $(".second_section").offset().top
  }, 1000);
})

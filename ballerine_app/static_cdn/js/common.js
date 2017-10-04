/**
 * Created by GeneralKenobi on 07.11.2016.
 */

$('.footer_p_to_insert').append("");
var now_date = new Date();
var after_date = new Date('December 28, 2016 00:00:00');

if(now_date < after_date){
    console.log(now_date);
    $('.footer_p_to_insert').append('<span class="pull-right"><span class="glyphicon glyphicon-heart" style="color:#FA2D3C"></span> Happy Bithday <span class="glyphicon glyphicon-heart" style="color:#FA2D3C"></span></span>')
}

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

});

$('.mouse-wheel').click(function () {
  $('html, body').stop().animate({
    scrollTop: $(".second_section").offset().top
  }, 1000);
})

/**
 * Created by GeneralKenobi on 11.11.2016.
 */
$document.scroll(function() {
  scrollTop = $document.scrollTop()

  if(scrollTop < 700){
    $('.first_section').css({
      backgroundPosition: 'center ' +  scrollTop*0.2 + 'px'
    })
  }
});
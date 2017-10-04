/**
 * Created by GeneralKenobi on 11.11.2016.
 */
$document.scroll(function() {
  scrollTop = $document.scrollTop()


  if(scrollTop < 700){
    $('.face_section').css({
      backgroundPosition: 'center ' + (-100 + scrollTop*0.2) + 'px'
    })
  }
});
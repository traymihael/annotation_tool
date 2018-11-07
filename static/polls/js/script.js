$(function() {
  var $win = $(window),
      $body = $('body'),
      $position_target = $('#position_target'),
      navPos = $position_target.offset().top,
      fixedClass = 'is-fixed',
      $clone_position_target = $position_target.clone(true);
  $clone_position_target.css('display', 'none');
  $clone_position_target.addClass(fixedClass);
  $clone_position_target.appendTo($body);


  $win.on('load scroll', function() {
    var value = $(this).scrollTop();
    if ( value > navPos ) {

      $clone_position_target.css('display', 'block');
    } else {

      $clone_position_target.css('display', 'none');
    }
  });
});
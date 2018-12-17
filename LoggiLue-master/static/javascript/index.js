//Menyn som försvinner
jQuery( document ).ready(function(){
    var header = document.querySelector("#menu_main");
    var headroom = new Headroom(header, {
        offset : 5,
        tolerance: {
          down : 10,
          up : 5
        },
        classes: {
          initial: "animated",
          pinned: "slideDown",
          unpinned: "slideUp"
        }
    });
    headroom.init();
});



//easing plugin för scroll
$(function() {
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1200, 'easeInOutExpo');
        event.preventDefault();
    });
});

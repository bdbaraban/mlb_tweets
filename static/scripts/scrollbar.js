$(document).ready(function () {
    $(".left").mCustomScrollbar({
         theme: "minimal"
    });
    $('.leftCollapse').on('click', function () {
        $('.left').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
    
    $(".right").mCustomScrollbar({
         theme: "minimal"
    });

    $('.rightCollapse').on('click', function () {
        $('.right').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

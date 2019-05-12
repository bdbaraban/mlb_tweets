$(document).ready(function () {
    $(".menu").mCustomScrollbar({
         theme: "minimal"
    });

    $('.menuCollapse').on('click', function () {
        $('.menu').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});
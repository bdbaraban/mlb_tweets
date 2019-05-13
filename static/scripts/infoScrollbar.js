$(document).ready(function () {
    $(".info").mCustomScrollbar({
         theme: "minimal"
    });

    $('.infoCollapse').on('click', function () {
        $('.info').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});
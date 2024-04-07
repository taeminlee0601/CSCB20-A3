$(document).ready(function() {
    $('.sidebar-shrinked').hide();

    $('.log-out').click(function() {
        $.ajax({
            url: '/logout',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({status: 'logged_out'}),
            success: function() {
                console.log('logged out successfully');
                window.location.href='/';
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });

    $('.menu-button').click(function() {
        if ($('.sidebar').hasClass('hidden')) {
            $('.sidebar').show();
            $('.sidebar').removeClass('hidden');
            $('.sidebar-shrinked').hide();
            $('body').removeClass('responsive-body');
        } else {
            $('.sidebar').hide();
            $('.sidebar').addClass('hidden');
            $('.sidebar-shrinked').show();
            $('body').addClass('responsive-body');
        }
    })
});
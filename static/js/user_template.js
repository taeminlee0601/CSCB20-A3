$(document).ready(function() {
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
});
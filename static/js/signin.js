$(document).ready(function(){
    function checkInputs() {
        var filled = true;
        $('.required').each(function() {
            // Check empty fields
            if ($(this).val() == '') {
                filled = false;
                return false;
            }
        });

        if (filled) {
            $('#sign').addClass('active');
        } else {
            $('#sign').removeClass('active');
        }
    }

    // Check when key is released
    $('.required').on('keyup', function() {
        checkInputs();
    });

    // Check on page load
    checkInputs();
});

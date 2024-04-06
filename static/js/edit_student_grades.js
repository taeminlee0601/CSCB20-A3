$(document).ready(function() {
    $('.stu-grade').click(function() {
        var sid = $(this).closest('tr').find('.sid').text();
        var aid = $(this).closest('tr').find('.aid').text();
        $(this).replaceWith('<span class="stu-grade"><input class="new-grade" type="text" /></span>');

        $('.new-grade').on('focusout keypress', function(e) {
            if (e.type == 'focusout' || (e.type == 'keypress' && (e.keyCode == 13 || e.keyPress == 13))) {
                var new_grade = $(this).val();
                if (new_grade > 100) {
                    new_grade = 100;
                }
                $.ajax({
                    url: 'http://127.0.0.1:5000/edit_grades',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ id: aid, sid: sid, new_grade: new_grade}),
                    success: function(new_url) {
                        console.log('Sent sucessfully');
                        $('.new-grade').replaceWith('<span class="stu-grade">' + new_grade + '</span>');
                        window.location.href='edit_grades';
                    },
                    error: function(error) {
                        console.log('Error:', error);
                    }
                });
            }
        });
    });
});

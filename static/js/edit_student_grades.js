$(document).ready(function() {
    $('.stu-grade').click(function() {
        $(this).replaceWith('<span class="stu-grade"><input class="new-grade" type="text" /></span>');

        $('.new-grade').on('focusout keypress', function(e) {
            if (e.type == 'keypress' && (e.keyCode == 13 || e.keyPress == 13)) {
                var new_grade = $('.new-grade').val();
                $.ajax({
                    url: 'http://127.0.0.1:5000/edit_student_grades.html',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ data: new_grade }),
                    success: function(new_url) {
                        console.log('Sent sucessfully');
                    },
                    error: function(error) {
                        console.log('Error:', error);
                    }
                });
            }

            if (e.type == 'focusout') {
                var new_grade = $('.new-grade').val();
                $.ajax({
                    url: 'http://127.0.0.1:5000/edit_student_grades.html',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ data: new_grade }),
                    success: function(new_url) {
                        console.log('Sent sucessfully');
                    },
                    error: function(error) {
                        console.log('Error:', error);
                    }
                });
            }
        });
    });

    $('.stu-grade').replaceWith('<span class="stu-grade">{{info[2]}}</span>');
});
$(document).ready(function() {
    $('.ass-manage-grades-btn').click(function() {
        var ass_id = $(this).closest('tr').find('.ass-id').text();
        $.ajax({
            url: 'http://127.0.0.1:5000/edit_grades',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ data: ass_id }),
            success: function(response) {
                console.log('Server response:', response);
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });

        window.location.href="edit_student_grades.html";
    });

    $('.exam-manage-grades-btn').click(function() {
        var exam_id = $(this).closest('tr').find('.exam-id').text();
        $.ajax({
            url: 'http://127.0.0.1:5000/edit_grades',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ data: exam_id }),
            success: function(response) {
                console.log('Server response:', response);
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });

        window.location.href="edit_student_grades.html";
    });
});
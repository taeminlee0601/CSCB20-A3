$(document).ready(function() {
    $('.delete-btn').click(function() {
        $(this).closest('tr').find('td').remove();
    });

    $('.add-btn').click(function() {
        $('.add-grade-box').show();
    });

    $('close-button').click(function() {
        $('.add-grade-box').hide();
    })
});
$(document).ready(function() {
    $(".ass-view-student-comment-btn").click(function() {
        $('#student-comment').show();
    });
    $('#close-button-1').click(function(){
        $('#student-comment').hide();
    });
})

$(document).ready(function() {
    $(".ass-add-comment-btn").click(function() {
        $('#add-comment-popup').show();
    });
    $('#close-button-2').click(function(){
        $('#add-comment-popup').hide();
    });
})
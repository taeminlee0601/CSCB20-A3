$(document).ready(function(){
    $('#view-comment-button').click(function(){
        $('#comment-content').show();
    });

    $('#close-button').click(function(){
        $('#comment-content').hide();
    });
});
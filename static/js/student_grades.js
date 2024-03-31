$(document).ready(function(){
    $("#remark-button").click(function(){
        $("#remark-content").show();
    });

    $('#close-button').click(function(){
        $('#remark-content').hide();
    });
});
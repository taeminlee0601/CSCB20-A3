// $(document).ready(function(){
//     $('.view-comment-button').click(function(){
//         $('#comment-content').show();
//         $('#comment-content p').text(function() {
//             console.log($(this).parent().parent().find('.comment').text());
//             return $(this).parent().parent().find('.comment').text()
//         });
//     });

//     $('#close-button').click(function(){
//         $('#comment-content').hide();
//         $('#comment-content p').text(function() {
//             return '';
//         });
//     });
// });

var comment_btn = Array.from(document.getElementsByClassName('view-comment-button'))
var view_comment = document.getElementById('comment-content');
var display = document.querySelector('#comment-content p');
comment_btn.forEach(function(element) {
    element.addEventListener('click', function() {
        view_comment.style.display = 'block'
        var par_tr = this.closest('tr');
        display.textContent = par_tr.querySelector('.comment').textContent;
    });
});

document.querySelector('#close-button').addEventListener('click', function() {
    view_comment.style.display = 'none';
    display.textContent = '';
});
$(document).ready(function() {
    $(".ass-view-student-comment-btn").click(function() {
        $('#student-comment-ass').show();
    });
    $('#close-button-1').click(function(){
        $('#student-comment-ass').hide();
    });
    $(".add-comment-btn").click(function() {
        $('#add-comment-popup').show();
    });
    $('#close-button-2').click(function(){
        $('#add-comment-popup').hide();
    });
    $('#close-button-2').click(function(){
        $('#add-comment-popup').hide();
    });
    $('.exam-view-student-comment-btn').click(function() {
        $('#student-comment-exam').show();
    });
    $('#close-button-3').click(function(){
        $('#student-comment-exam').hide();
    });
});

data = {}
var btn_add_comment_arr = Array.from(document.getElementsByClassName('add-comment-btn'));
var btn_clicking, func_clicking;
btn_add_comment_arr.forEach(function(element) {
    element.addEventListener('click', function click() {
        data['id'] = this.closest('tr').querySelector('.regrade-request-id').textContent;
        
        var assessmentListBox = this.closest('.assessment-list-box');
        if (assessmentListBox.querySelector('h2').textContent === 'Assignments') {
            data['assessment-type'] = 'a';
        } else if (assessmentListBox.querySelector('h2').textContent === 'Exams') {
            data['assessment-type'] = 'e';
        }
        btn_clicking = element;
        func_clicking = click;
    });
});

document.getElementById('submit-comment-btn').addEventListener('click', function() {
    data['desc'] = this.closest('form').querySelector('textarea').value;
    fetch('/manage_remark_request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            // TODO: disable the button after send remark req 
            console.log('Data submitted successfully');
        } else {
            console.error('Failed to submit data');
        }
    }).catch(error => {
        console.log('Error: ', error);
    })
});

document.getElementById('add-comment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    this.querySelector('textarea').value = '';
    $('#add-comment-popup').hide();
});
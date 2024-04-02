$(document).ready(function(){
    $(".remark-button").click(function(){
        $("#remark-content").show();
    });
    $('#close-button').click(function(){
        $('#remark-content').hide();
    });
});


data = {}
var btn_remark_arr = Array.from(document.getElementsByClassName('remark-button'));
var btn_clicking, func_clicking;
btn_remark_arr.forEach(function(element) {
    element.addEventListener('click', function click() {
        data['id'] = this.closest('tr').querySelector('.grade-id').textContent;
        
        var assessmentListBox = this.closest('.assessment-list-box');
        data['document-type'] = assessmentListBox.querySelector('h2').textContent;
        btn_clicking = element;
        func_clicking = click;
    });
});


document.getElementById('submit-regrade-request-btn').addEventListener('click', function() {
    data['desc'] = this.closest('form').querySelector('textarea').value;
    fetch('/remark_request', {
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

document.getElementById('regrade-request-form').addEventListener('submit', function(event) {
    event.preventDefault();
    this.querySelector('textarea').value = '';
    $('#remark-content').hide();
});
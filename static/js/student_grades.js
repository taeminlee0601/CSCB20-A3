$(document).ready(function(){
    $("#remark-button").click(function(){
        $("#remark-content").show();
    });
    $('#close-button').click(function(){
        $('#remark-content').hide();
    });
});

data = {}
document.getElementsByClassName('remark-request').addEventListener('click', function() {
    data['name'] = document.querySelector('td:nth-child(1)').textContent;
    data['grade'] = document.querySelector('td:nth-child(2)').textContent;
    data['due_date'] = document.querySelector('td:nth-child(3)').textContent;
    
    var assessmentListBox = this.closest('.assessment-list-box');
    data['document-type'] = assessmentListBox.querySelector('h2').textContent;
});

document.getElementById('submit-regrade-request-btn').addEventListener('click', function() {
    fetch('127.0.0.1:5000/remark_request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            console.log('Data submitted successfully');
        } else {
            console.error('Failed to submit data');
        }
    }).catch(error => {
        console.log('Error: ', error);
    })
});
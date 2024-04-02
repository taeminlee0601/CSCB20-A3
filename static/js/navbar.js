function menuBarClicked(menuButton, tabGrid) {
    menuButton.classList.toggle("menuButtonOnClick");
    tabGrid.classList.toggle("tabGridAppear");

    var dropdownContents = document.getElementsByClassName("dropdown-content-mobile");

    for (var i = 0; i < dropdownContents.length; i++) {
        var current = dropdownContents[i]
        if (current.classList.contains("closeDropdown")) {
            current.classList.remove("closeDropdown");
        }
    }
}

function showDropdown(dropdownContent) {
    dropdownContent.classList.toggle("showDropdown");

    var dropdownContents = document.getElementsByClassName("dropdown-content-mobile");

    for (var i = 0; i < dropdownContents.length; i++) {
        var current = dropdownContents[i];
        if (current !== dropdownContent && current.classList.contains("showDropdown")) {
            current.classList.remove("showDropdown");
        }
    }
}

data = {}
document.getElementById('logout').addEventListener('click', function() {
    data['desc'] = 'logoutpls';
    fetch('/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            // TODO: disable the button after send remark req 
            console.log('Data submitted successfully');
            window.location.href = '/';
        } else {
            console.error('Failed to submit data');
        }
    }).catch(error => {
        console.log('Error: ', error);
    })
});

document.getElementById('logout-mobile').addEventListener('click', function() {
    data['desc'] = 'logoutpls';
    fetch('/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            // TODO: disable the button after send remark req 
            console.log('Data submitted successful');
            window.location.href = '/';
        } else {
            console.error('Failed to submit data');
        }
    }).catch(error => {
        console.log('Error: ', error);
    })
});
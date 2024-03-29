var numClicked = 0;

function menuBarClicked(menuButton, tabGrid) {
    numClicked++;
    menuButton.classList.toggle("menuButtonOnClick");
    tabGrid.classList.toggle("tabGridAppear");

    var dropdownContents = document.getElementsByClassName("dropdown-content-mobile");

    if (numClicked % 2 == 0) {
        for (var i = 0; i < dropdownContents.length; i++) {
            var current = dropdownContents[i]
            if (current.classList.contains("showDropdown")) {
                current.classList.remove("showDropdown");
            }
        }
    } else {
        for (var i = 0; i < dropdownContents.length; i++) {
            var current = dropdownContents[i]
            if (current.classList.contains("closeDropdown")) {
                current.classList.remove("closeDropdown");
            }
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
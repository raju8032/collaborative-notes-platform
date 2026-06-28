window.onload = function () {
    alert("Welcome to Team Management System!");
    updateMemberCount();
};

// Add Member
function addMember() {

    let name = prompt("Enter Member Name");

    if (name == "" || name == null) {
        return;
    }

    let table = document.getElementById("memberTable");

    // Duplicate Check
    for (let i = 1; i < table.rows.length; i++) {

        let existingName = table.rows[i].cells[0].innerText.trim().toLowerCase();

        if (existingName == name.trim().toLowerCase()) {
            alert("Member already exists!");
            return;
        }

    }

    let row = table.insertRow();

    row.innerHTML =
        "<td>" + name + "</td>" +
        "<td><select onchange='changeRole(this)'>" +
        "<option>Owner</option>" +
        "<option>Admin</option>" +
        "<option selected>Member</option>" +
        "</select></td>" +
        "<td><button onclick='removeMember(this)'>Remove</button></td>";

    updateMemberCount();

}

// Remove Member
function removeMember(button) {

    let row = button.parentNode.parentNode;

    let role = row.cells[1].querySelector("select").value;

    if (role == "Owner") {
        alert("Owner cannot be removed!");
        return;
    }

    if (confirm("Do you want to remove this member?")) {

        row.remove();

        updateMemberCount();

    }

}

// Change Role
function changeRole(selectBox) {

    let table = document.getElementById("memberTable");

    let ownerCount = 0;

    for (let i = 1; i < table.rows.length; i++) {

        let currentRole = table.rows[i].cells[1].querySelector("select").value;

        if (currentRole == "Owner") {
            ownerCount++;
        }

    }

    let name = selectBox.parentNode.parentNode.cells[0].innerText;

    let role = selectBox.value;

    if (role == "Owner" && ownerCount > 1) {

        alert("Only one Owner is allowed!");

        selectBox.value = "Member";

        return;

    }

    if (role == "Owner") {

        alert(name + " promoted to Owner");

    }

    else if (role == "Admin") {

        alert(name + " promoted to Admin");

    }

    else {

        alert(name + " changed to Member");

    }

}

// Search Member
function searchMember() {

    let input = document.getElementById("searchBox").value.toLowerCase();

    let table = document.getElementById("memberTable");

    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {

        let name = rows[i].cells[0].innerText.toLowerCase();

        if (name.includes(input)) {

            rows[i].style.display = "";

        }

        else {

            rows[i].style.display = "none";

        }

    }

}

// Member Counter
function updateMemberCount() {

    let table = document.getElementById("memberTable");

    let count = table.rows.length - 1;

    document.getElementById("memberCount").innerText = "Total Members: " + count;

}

function accessControl() {

    let role = document.getElementById("currentUserRole").value;

    let addBtn = document.querySelector("button");

    let removeBtns = document.querySelectorAll("button");

    let selects = document.querySelectorAll("select");

    if(role=="Owner"){

        addBtn.disabled=false;

        for(let i=0;i<removeBtns.length;i++){
            removeBtns[i].disabled=false;
        }

        for(let i=1;i<selects.length;i++){
            selects[i].disabled=false;
        }

        alert("Logged in as OWNER");

    }

    else if(role=="Admin"){

        addBtn.disabled=false;

        for(let i=0;i<removeBtns.length;i++){
            removeBtns[i].disabled=false;
        }

        for(let i=1;i<selects.length;i++){
            selects[i].disabled=true;
        }

        alert("Logged in as ADMIN");

    }

    else{

        addBtn.disabled=true;

        for(let i=0;i<removeBtns.length;i++){
            removeBtns[i].disabled=true;
        }

        for(let i=1;i<selects.length;i++){
            selects[i].disabled=true;
        }

        alert("Logged in as MEMBER");

    }

}

updateMemberCount();
accessControl();
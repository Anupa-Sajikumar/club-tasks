const validCredentials = [{username: "user1", password: "pass1"}, {username: "user2", password: "pass2"}];
const form = document.querySelector("form");
form.addEventListener("submit", (event) => {
    event.preventDefault();
    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;
    let isValid = false;
    for (let i = 0; i < validCredentials.length; i++) {
        if (validCredentials[i].username === username && validCredentials[i].password === password) {
            isValid = true;
            break;
        }
    }
    if (isValid) {
        window.location.href = "success.html";
    } else {
        alert("Username and password are incorrect.");
    }
});
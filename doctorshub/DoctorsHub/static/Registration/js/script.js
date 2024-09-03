

let resultElement = document.getElementById("result");

function isUsernameValid(username){
    if (username === "") {
        resultElement.innerHTML = "Enter Username*";
        return false;
    } 
    else if (username.length < 6) {
        resultElement.innerHTML = "Username must be at least six characters :(";
        return false;
    }  
    else if (!isNaN(username)) {
        resultElement.innerHTML = "Username must be string :(";
        return false;
    } 
    return true;
}

function isEmailValid(email){
    if (email === "") {
        resultElement.innerHTML = "Enter Your Email*";
        return false;
    } 
    else if(!email.includes("@gmail.com")){
        resultElement.innerHTML = "Your Email Not Valid :(";
        return false;
    }
    return true;
}

function isPasswordValid(password){
    var nums = /\d/;
    var specialCharacters = /[!@#$%^&*(),.?":{}|<>]/;

    if (password === "") {
        resultElement.innerHTML = "Enter Your Password*";
        return false;
    } 
    else if (password.length < 6) {
        resultElement.innerHTML = "Password must be at least 6 characters :(";
        return false;
    }
    else if(!nums.test(password) && !specialCharacters.test(password)){
        resultElement.innerHTML = "Enter a stronger password :(";
        return false;
    }
    return true;
}

function checkOnConfirmPassword(cPassword , password){
    if (cPassword === "") {
        resultElement.innerHTML = "Enter Confirm Password*";
        return false;
    } 
    else if (cPassword !== password) {
        resultElement.innerHTML = "Passwords do not match :(";
        return false;
    }
    return true;
}

function validation() {
    var password = document.Formfile.Password.value;
    var cPassword = document.Formfile.cPassword.value;
    var username = document.Formfile.Username.value;
    var email = document.Formfile.Email.value;
    if(isUsernameValid(username) && isEmailValid(email) && isPasswordValid(password) && checkOnConfirmPassword(cPassword , password)){
        return true;
    }
    return false;
}


function showPopupIfPasswordsMatch(event) {
    if(validation()){
        var popup = document.getElementById('popup');
            popup.classList.add('open-slide');
            event.preventDefault();
    }
}

function CloseSlide() {
    var popup = document.getElementById('popup');
    popup.classList.remove('open-slide');
    document.Formfile.submit();
    // window.location.href = './signUp.html';
}



function validation_login() {
    var password = document.Formfile.Password.value;
    var email = document.Formfile.Email.value;
    if (password === "") {
        resultElement.innerHTML = "Enter Your Password*";
        return false;
    } 
    if(isEmailValid(email)){
        return true;
    }
    return false;
}


function showPopupIfPasswordsMatch(event) {
    if(validation()){
        var popup = document.getElementById('popup');
            popup.classList.add('open-slide');
            event.preventDefault();
    }
}

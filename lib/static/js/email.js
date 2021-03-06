/*jshint esversion: 6 */
// connecting the contact email with my gmail account using emailJs
function sendMail() {
    emailjs.send("service_bbmb42t","build_connected",{
        "company_name": document.getElementById("company_name").value,
        "email_from": document.getElementById("email_from").value,
        "company_name_to": document.getElementById("company_name_to").value,
        "email_to": document.getElementById("email_to").value,
        "message": document.getElementById("message").value
    })
    .then (
        function(response) {
            console.log("success", response);
            messageSuccess();
        },
        function(error) {
            console.log("error", error);
            messageError();
        });
}
let submitEmail = document.getElementById("submit_email");
submitEmail.addEventListener("click", checkForm);

function checkForm(event) {
    event.preventDefault();
    let fromName = document.getElementById("company_name").value;
    let fromEmail = document.getElementById("email_from").value;
    let toName = document.getElementById("company_name_to").value;
    let toEmail = document.getElementById("email_to").value;
    let message = document.getElementById("message").value;
    let validFromEmail = validateEmail(fromEmail);
    let validToEmail = validateEmail(toEmail);
    if (fromEmail != toEmail) {
        if(fromName && validFromEmail && toName && validToEmail && message) {
            sendMail();
        } else {
            messageMissingField(fromName, validFromEmail, toName, validToEmail, message);
        }
    } else {
        messageSameEmail();
    }
}

//function taken from stack overflow
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

function messageMissingField(fromName, validFromEmail, toName, validToEmail, message) {
    if(!fromName){
        $(".swal-overlay").css("display", "block");
        swal({
            title: "Error!",
            icon: "info",
            text: `Please enter Company Name`,
            button: "OK",
        });
    } else if(!validFromEmail) {
        $(".swal-overlay").css("display", "block");
        swal({
            title: "Error!",
            icon: "info",
            text: `Please enter your valid email address`,
            button: "OK",
        });
    } else if(!toName){
        $(".swal-overlay").css("display", "block");
        swal({
            title: "Error!",
            icon: "info",
            text: `Please enter Receiver Name`,
            button: "OK",
        });
    } else if(!validToEmail) {
        $(".swal-overlay").css("display", "block");
        swal({
            title: "Error!",
            icon: "info",
            text: `Please enter a valid receiver email address`,
            button: "OK",
        });
    } else {
        $(".swal-overlay").css("display", "block");
        swal({
            title: "Error!",
            icon: "info",
            text: `Please enter a message`,
            button: "OK",
        });
    }
}
function messageSuccess() {
    emailSuccessMsg = document.getElementById("email-success-container");
    emailSuccessMsg.style.display = "block";

    emailSuccessOkBtn = document.getElementById("email-success-ok-btn");
    emailSuccessOkBtn.addEventListener("click", function() {
        emailSuccessMsg.style.display = "none";
    });
    /*$(".swal-overlay").css("display", "block");
    swal({
        title: "Success!",
        icon: "success",
        text: `Your email has been sent`,
        button: "OK",
    });*/
    
}

function messageError() {
    $(".swal-overlay").css("display", "block");
    swal({
        title: "Error!",
        icon: "error",
        text: `there was a problem! Your email has not been sent`,
        button: "OK",
    });
}

function messageSameEmail() {
    $(".swal-overlay").css("display", "block");
    swal({
        title: "Error!",
        icon: "error",
        text: `Error. Sender and receiver email addresses have to be different`,
        button: "OK",
    });
}
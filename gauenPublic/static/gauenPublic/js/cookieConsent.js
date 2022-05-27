/*
 * Bootstrap Cookie Alert by Wruczek
 * https://github.com/Wruczek/Bootstrap-Cookie-Alert
 * Released under MIT license
 */
var acceptCookies = document.querySelector(".acceptcookies");
var acceptAllCookies = document.querySelector(".acceptallcookies");
var selectedCookies = document.querySelector(".selectedcookies");


acceptCookies.addEventListener("click", function () {

    $.ajax({
        url : "http://127.0.0.1:8000/cookies/",
        type : "GET", // http method
        data : {
          csrfmiddlewaretoken: '{{ csrf_token }}',//This is must for security in Django
        }, // data sent with the post request
    
        // handle a successful response
        success : function(response){
        },
    
        // handle a non-successful response
        error : function() {
        console.log("ruim")
        }
    });
    //setCookie("acceptCookies", true, 365);
    cookieAlert.classList.remove("show");

    // dispatch the accept event
    window.dispatchEvent(new Event("cookieAlertAccept"))
});




acceptAllCookies.addEventListener("click", function () {

    $.ajax({
        url : "http://127.0.0.1:8000/cookies/",
        type : "GET", // http method
        data : {
          csrfmiddlewaretoken: '{{ csrf_token }}',//This is must for security in Django
        }, // data sent with the post request
    
        // handle a successful response
        success : function(response){
        },
    
        // handle a non-successful response
        error : function() {
        console.log("ruim")
        }
    });
    //setCookie("acceptCookies", true, 365);
    cookieAlert.classList.remove("show");

    // dispatch the accept event
    window.dispatchEvent(new Event("cookieAlertAccept"))
});


selectedCookies.addEventListener("submit", function (event) {

    $.ajax({
        url : "http://127.0.0.1:8000/cookies/",
        type : "POST", // http method
        data : {
            csrfmiddlewaretoken: '{{ csrf_token }}',//This is must for security in Django
        }, // data sent with the post request
    
        // handle a successful response
        success : function(response){
        },
    
        // handle a non-successful response
        error : function() {
        console.log("ruim")
        }
    });
    //setCookie("acceptCookies", true, 365);
    cookieAlert.classList.remove("show");

    // dispatch the accept event
    window.dispatchEvent(new Event("cookieAlertAccept"))
});
//function to call other function when the pag loads
function callFunctions() {
    //function to show user time
    time();
}


//funtion to get real time
function time() {
    var date = new Date();
    var hour = date.getHours();
    var minutes = date.getMinutes();

    document.getElementById('user-time').innerHTML = ""+ hour + "<span>:</span>" + minutes;setTimeout('time()', 60000);
}

/**
 * Verificar idioma do usuario - verify user language
 */
function userLanguage() {
    if (navigator.browserLanguage) {
        var idioma = navigator.browserLanguage;
    } else if (navigator.language) {
        var idioma = navigator.language;
    }

    alert("Your language is:" + idioma);
}
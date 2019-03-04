
//function to call other function when the pag loads
function callFunctions() {
    time();
}

//funtion to get real time
function time() {
    var date = new Date();
    var hour = date.getHours();
    var minutes = date.getMinutes();

    document.getElementById('user-time').innerHTML = " <span>Hour</span> " + hour + " <span>Minutes</span> " + minutes; setTimeout('time()', 60000);
}
/*
* Quando o scroll desder 20px to topo do documento, irá exibir o butão
* When the user scrolls down 20px from the top of the document, show the button
*/
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btnTop").style.display = "block";
    } else {
        document.getElementById("btnTop").style.display = "none";
    }
}
// Quando clicar no butão, rolar para o topo da tela
// When the user clicks on the button, scroll to the top of the document
function btnTop() {
    document.body.scrollTop = 0; //  Para o safari - For Safari
    document.documentElement.scrollTop = 0; // Para o chrome, IE e Opera - For Chrome, Firefox, IE and Opera
}

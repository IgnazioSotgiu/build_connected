$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    document.getElementById("year").innerHTML = new Date().getFullYear();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy"
    });
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    });

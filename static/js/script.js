$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    document.getElementById("year").innerHTML = new Date().getFullYear();
    $('select').formSelect();
  });
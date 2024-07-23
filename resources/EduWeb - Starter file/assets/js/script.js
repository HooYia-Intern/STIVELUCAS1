'user strict'
const addEventOnElem = function (eleo, type, callback){
    if(eleo.length  >  1){
        for (let i = 0 ; i < eleo.length;  i++){
            eleo[i].addEventListener(type, callback);
        }
    }
    else{
        eleo.addEventListener(type, callback);
    }
}
// navbar
const navbar = document.querySelector("[data-navbar]") ;
const navtogglers = document.querySelectorAll ("[ data-nav-toggler]");
const navlinks = document.querySelectorAll("[data-nav-link]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function (){
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
}
addEventOnElem(navtogglers, "click", toggleNavbar);
//fonctionnalite qui permet d'entrer des elements dans le screen de la claculatrice
var screen=document.querySelector('#screen');
var btn=document.querySelectorAll('.btn');

for(item of btn){
    item.addEventListener('click' ,(e)=> {
        btntext=e.target.innerText;
        screen.value+=btntext;
    });
}

//fonction pour les opreration trigonometrique
function sin(){
    screen.value=Math.sin(screen.value);
}

function cos(){
    screen.value=Math.cos(screen.value);
}


function tan(){
    screen.value=Math.tan(screen.value);
}


//fonction de la puissance de 2
function power(){
    screen.value=Math.pow(screen.value,2);
}

//fonction pour la racine carrer
function squart(){
    screen.value=Math.sqrt(screen.value,2);
}

//fonction pour le logarithme
function log(){
    screen.value=Math.log(screen.value);
}


//fobction d'attribution des valeurs api et exponentielle
function pi(){
    screen.value=3.14159265359;
}

function exp(){
    screen.value=2.71828182846;
}


//fonction pour le calcul des factoriel d'un nombre
function fact(){
    var i, num, f;
    f=1
    num=screen.value;
    for(i=1; i<=num; i++){
        f=f*i;
    }
    i=i-1;
    screen.value=f;

}

//fonction pour la suppression des elements
function space(){
    screen.value=screen.value.substr(0,screen.value.length-1);
}

function spaceall(){
    screen.value='';
}

const buscar = document.getElementById('buscar-2')
var pokes;

document.addEventListener('DOMContentLoaded',(e)=>{fetchData()})
const fetchData = async()=>{
    console.log(document.getElementById('pokes').value.replace("'",'"'))
    pokes = JSON.parse(document.getElementById('pokes').value);
    console.log(pokes)
}
function filtro(){
    var pokefiltro;
    for(poke of pokes){
        buscar.indexOf(poke.name)
            console.log(poke)
        
    }
}

buscar.addEventListener('keyup',function(){
    filtro()
})
const searchbar = document.getElementById('pokenames')
const pokeid = document.getElementById('pokeid').innerHTML
searchbar.addEventListener('click',function(){
    // window.location.href = "http://www.w3schools.com";
    var url = window.location.origin
    if (searchbar.value != pokeid && searchbar.value!=0 ){
        window.location.href = url + "/menu/"+searchbar.value}
})
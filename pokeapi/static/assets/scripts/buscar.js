const searchbar = document.getElementById('pokenames')

searchbar.addEventListener('click',function(){
    // window.location.href = "http://www.w3schools.com";
    var url = window.location.origin
    window.location.href = url + "/menu/"+searchbar.value
})
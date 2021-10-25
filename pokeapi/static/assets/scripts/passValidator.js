const form = document.getElementById('reg-form')
const boton = document.getElementById('boton')
const p1 = document.getElementById('p1')
const p2 = document.getElementById('p2')
boton.addEventListener('click',function(){
    console.log(p1.value,p2.value)

    if(p1.value != p2.value) {
        document.getElementById('msg-contra').hidden = false
    }
    if (p1.value === p2.value){form.submit();}

})
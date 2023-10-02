const zBlure  = document.getElementById('zBlure')
const editeInfo  = document.getElementById('editeInfo')
const select  = document.getElementById('select')
const openSelect = document.getElementById('openSelect')
const openEditeInfo = document.getElementById('openEditeInfo')
let cancelKey = document.querySelectorAll('.cancel')
console.log(cancelKey);

 cancelKey.forEach(e => 
    e.addEventListener('click',()=>  {select.classList.add('hidden')  
    editeInfo.classList.add('hidden')
    zBlure.classList.remove('blur-sm')}
 ));

openSelect.addEventListener('click', () =>{
    select.classList.remove('hidden')
    select.classList.add('grid')
zBlure.classList.add('blur-sm')
})

openEditeInfo.addEventListener('click', ()=>{
    editeInfo.classList.remove('hidden')

})
function cancelHandler () {
    select.classList.add('hidden')  
    editeInfo.classList.add('hidden')
    zBlure.classList.remove('blur-sm')
}


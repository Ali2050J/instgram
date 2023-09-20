let $ = document
const fllowers = $.getElementById('Fllowers')
const postBox = $.getElementById('postBox')
const forhr = $.getElementById('forhr')
const iconTagged = $.getElementById('iconTagged') 
const iconSave = $.getElementById('iconSave')
const usertitle = $.getElementById('usertitle')
const iconPost = $.getElementById('iconPost')
const blure = $.getElementById('blure')
const buttombar = $.getElementById('buttombar')
const clickMenu = $.getElementById('clickMenu')

let flag = null;
clickMenu.addEventListener('click',()=>{
    buttombar.classList.add('flex')
    buttombar.classList.remove('hidden')
    blure.classList.add('blur-sm')

})
blure.addEventListener('click',()=>{
    buttombar.classList.add('hidden')
    buttombar.classList.remove('flex')
    blure.classList.remove('blur-sm')
},true)



iconPost.addEventListener('click', ()=>{
    forhr.classList.add('justify-start')
    forhr.classList.remove('justify-end')
    forhr.classList.remove('justify-center')
    postBox.innerHTML = `
    <div class="w-full sm:h-52 md:h-64 h-36 xl:h-80 overflow-hidden">
    <img class=" object-cover sm:h-[400px] sm:w-[400px] md:h-[450px] md:w-[450px] lg:w-[550px] lg:h-[550px] xl:w-[600px] xl:h-[800px]  "  src="/1247179.webp" alt="#">

    </div>
    <div class="w-full sm:h-52 md:h-64 h-36 xl:h-80 overflow-hidden">
    <img class=" object-cover sm:h-[400px] sm:w-[400px] md:h-[450px] md:w-[450px] lg:w-[550px] lg:h-[550px] xl:w-[600px] xl:h-[800px]  "  src="/PRI1.jpg" alt="#">

    </div>
    `})
iconSave.addEventListener('click',()=> {
    forhr.classList.add('justify-center')
    forhr.classList.remove('justify-end')
    forhr.classList.remove('justify-start')
    postBox.innerHTML = ` 
    <div class="w-full sm:h-52 md:h-64 h-36 xl:h-80 overflow-hidden">
    <img  class=" object-cover sm:h-[340px] sm:w-[340px] md:h-[450px] md:w-[450px]  "  src="/6f949f4e7cf50c42c780bb30f303eddb3083f1213a8f4cb06b5673f79025e0a7._RI_.jpg" alt="#">

    </div>


    `
    
})
iconTagged.addEventListener('click',()=>{
    forhr.classList.add('justify-end')
    forhr.classList.remove('justify-center')
    forhr.classList.remove('justify-start')
    postBox.innerHTML = ''
})







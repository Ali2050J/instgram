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
const postBoxSave = $.getElementById('postBoxSave')
const zBlure = document.getElementById('zBlure')
const editeInfo = document.getElementById('editeInfo')
const select = document.getElementById('select')
const openSelect = document.getElementById('openSelect')
const openEditeInfo = document.getElementById('openEditeInfo')
let cancelKey = document.querySelectorAll('.cancel')
const main = document.getElementById('main')
const sBlure = document.getElementById('sBlure')
var post = document.querySelectorAll("[id='post']");
var favorite_post = document.querySelectorAll("[id='favorite-post']");

let flag;
clickMenu.addEventListener('click', () => {
    buttombar.classList.add('flex')
    buttombar.classList.remove('hidden')
    blure.classList.add('blur-sm')
    flag = true
})
window.addEventListener('click', () => {
    if (flag == true) {
        buttombar.classList.add('hidden')
        buttombar.classList.remove('flex')
        blure.classList.remove('blur-sm')
        flag = false
    }
}, true)



iconPost.addEventListener('click', () => {

    forhr.classList.add('justify-start')
    forhr.classList.remove('justify-end')
    postBox.classList.add('grid')
    postBox.classList.remove('hidden')
    postBoxSave.classList.add('hidden')
    postBoxSave.classList.remove('grid')
}
)
iconSave.addEventListener('click', () => {
    forhr.classList.add('justify-end')
    forhr.classList.remove('justify-start')
    postBoxSave.classList.add('grid')
    postBoxSave.classList.remove('hidden')
    postBox.classList.add('hidden')
    postBox.classList.remove('grid')
})

let post_modals = post;

let favorite_post_modals = favorite_post;

for (var i = 0; i < post_modals.length; i++) {
    post_modals[i].addEventListener('click', () => {
        zBlure.classList.remove('hidden');
        blure.classList.add('blur-sm');
        sBlure.classList.add('blur-sm');
    });
}


for (var i = 0; i < favorite_post_modals.length; i++) {
    favorite_post_modals[i].addEventListener('click', () => {
        zBlure.classList.remove('hidden');
        blure.classList.add('blur-sm');
        sBlure.classList.add('blur-sm');    
    });
}


////modal/

cancelKey.forEach(e =>
    e.addEventListener('click', () => {
        select.classList.add('hidden')
        editeInfo.classList.add('hidden')
        zBlure.classList.remove('blur-sm')
        zBlure.classList.add('hidden')
        blure.classList.remove('blur-sm')
        sBlure.classList.remove('blur-sm')
    }

    ));

openSelect.addEventListener('click', () => {
    select.classList.remove('hidden')
    select.classList.add('grid')
    zBlure.classList.add('blur-sm')
    blure.classList.add('blur-sm')
    sBlure.classList.add('blur-sm')
})

openEditeInfo.addEventListener('click', () => {
    editeInfo.classList.remove('hidden')
    blure.classList.add('blur-sm')
    zBlure.classList.add('blur-sm')
    sBlure.classList.add('blur-sm')

})

function readyss() { 
    if (postBox.innerHTML.replace(/[\r\n\s]/gm, '') == '') { 
        postBox.classList.remove('grid-col-3') 
        postBox.classList.add('grid-col-1') 
        postBox.innerHTML = `<div class=" w-[100rem] h-96  "><h1 class="font-bold p-4 xl:ml-[23%] lg:ml-[20%] mt-16 md:ml-[15%] ml-[5%] sm:ml-[8%] text-slate-400 text-5xl mx-auto flex content-center black">You dont have any post</h1></div> 
        ` 
    } 
} 
function readyss2() { 
    if (postBoxSave.innerHTML.replace(/[\r\n\s]/gm, '') == '') { 
        postBoxSave.classList.remove('grid-col-3') 
        postBoxSave.classList.add('grid-col-1') 
 
        postBoxSave.innerHTML = `<div class=" w-[100rem]  h- overflow-hidden"><h1 class="font-bold xl:ml-[23%] lg:ml-[20%] mt-16 md:ml-[15%] ml-[5%] sm:ml-[8%] text-slate-400 text-5xl mx-auto flex content-center black">You dont have any post</h1></div> 
        ` 
    } 
 
} 
readyss2(); 
readyss();

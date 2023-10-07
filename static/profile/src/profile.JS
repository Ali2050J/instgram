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
const postBoxSave =$.getElementById('postBoxSave')
const zBlure  = document.getElementById('zBlure')
const editeInfo  = document.getElementById('editeInfo')
const select  = document.getElementById('select')
const openSelect = document.getElementById('openSelect')
const openEditeInfo = document.getElementById('openEditeInfo')
let cancelKey = document.querySelectorAll('.cancel')
const main = document.getElementById('main')
 const sBlure = document.getElementById('sBlure')
 let postcount = document.getElementById('postcunt')
 let imgside = document.querySelectorAll('.imgside')
 let disc = document.querySelectorAll('.disc')
 let likeCunt = document.getElementById('likeCunt')
let flag;

clickMenu.addEventListener('click',()=>{
    buttombar.classList.add('flex')
    buttombar.classList.remove('hidden')
    blure.classList.add('blur-sm')
    flag = true
})
window.addEventListener('click',()=>{
    if (flag == true) {
        
    
    buttombar.classList.add('hidden')
    buttombar.classList.remove('flex')
    blure.classList.remove('blur-sm')
    flag = false
}
},true)



iconPost.addEventListener('click', ()=>{

    forhr.classList.add('justify-start')
    forhr.classList.remove('justify-end')
 postBox.classList.add('grid')
 postBox.classList.remove('hidden')
 postBoxSave.classList.add('hidden')
 postBoxSave.classList.remove('grid')
    


}
)
iconSave.addEventListener('click',()=> {
 

        
    
    forhr.classList.add('justify-end')

    forhr.classList.remove('justify-start')
    postBoxSave.classList.add('grid')
    postBoxSave.classList.remove('hidden')
    postBox.classList.add('hidden')
    postBox.classList.remove('grid')


    
    
})

let testmodals = postBox 

let testmodals2 = postBoxSave 

testmodals.addEventListener('click', ()=>{
    zBlure.classList.remove('hidden')
    blure.classList.add('blur-sm')
    sBlure.classList.add('blur-sm')
})
testmodals2.addEventListener('click', ()=>{
    zBlure.classList.remove('hidden')
    blure.classList.add('blur-sm')
    sBlure.classList.add('blur-sm')
})




////modal/
cancelKey.forEach(e => 
    e.addEventListener('click',(e)=>  {
        select.classList.add('hidden')  
        
    
    editeInfo.classList.add('hidden')
  zBlure.classList.remove('blur-sm')
    zBlure.classList.add('hidden')
  blure.classList.remove('blur-sm')
  sBlure.classList.remove('blur-sm')
    
}

 ));

openSelect.addEventListener('click', () =>{
    select.classList.remove('hidden')
    select.classList.add('grid')
zBlure.classList.add('blur-sm')
blure.classList.add('blur-sm')
sBlure.classList.add('blur-sm')
})

openEditeInfo.addEventListener('click', ()=>{
    editeInfo.classList.remove('hidden')
    blure.classList.add('blur-sm')
    zBlure.classList.add('blur-sm')
    sBlure.classList.add('blur-sm')

})

function readyss() {
    if (postBox.innerHTML == '') {
        postBox.classList.remove('grid-col-3')
        postBox.classList.add('grid-col-1')

        postBox.innerHTML = `        <div class=" w-[100rem] h-96  "><h1 class="font-bold p-4 xl:ml-[23%] lg:ml-[20%] mt-16 md:ml-[15%] ml-[5%] sm:ml-[8%] text-slate-400 text-5xl mx-auto flex content-center">Photos of you</h1></div>
        `
    }
}
function readyss2() {
    if (postBoxSave.innerHTML == '') {
        postBoxSave.classList.remove('grid-col-3')
        postBoxSave.classList.add('grid-col-1')

        postBoxSave.innerHTML = `           <div class=" w-[100%] h-96  "><h1 class="font-bold p-4 xl:ml-[23%] lg:ml-[20%] mt-16 md:ml-[15%] ml-[5%] sm:ml-[8%] text-slate-400 text-5xl mx-auto flex content-center">Photos of you</h1></div>
        `
    }

}
readyss2();
    readyss();

let postsAray = []


   async function getHandeler() {
    
     await fetch('https://instagram.iran.liara.run/api/posts/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        mode: 'cors',
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not OK');
        }
    })
    .then(data => {
        console.log(data);
      postsAray = data
      setPostCunt()
      console.log(postsAray[0]);
      postsAray.forEach(da => {
              postBox.insertAdjacentHTML("afterbegin",`
      <div style="
      background-image: url('https://instagram.iran.liara.run/${da.image}'); /* آدرس تصویر */
      background-size: cover; /* تنظیم اندازه تصویر */
      background-position: center; /* تنظیم موقعیت تصویر */
    
    " key="${da.id}" onclick="modalsHandeler(event)" class=" wow wow slideInLeft rese overflow-hidden w-full xl:h-80 lg:h-72 md:h-64 sm:h-52 h-48 ">
        </div>
      `)
      console.log(da);

      });


    })
    .catch(error => {
        console.error('Error:', error);
    });
   }
    
    getHandeler()

    
function modalsHandeler(e){
let post = e.target


modalClickOpen(post.getAttribute("key"))
} 


function modalClickOpen(key) {
        
console.log('key');
console.log(imgside);
imgside.forEach(ee => {
    ee.setAttribute("style",`
    background-image: url('https://instagram.iran.liara.run/${postsAray[key-1].image}'); /* آدرس تصویر */
    background-size: cover; /* تنظیم اندازه تصویر */
    background-position: center; /* تنظیم موقعیت تصویر */
  `) 
});
disc.forEach( ee => {
    ee.innerHTML = postsAray[key-1].caption
}

) 
likeCunt.innerHTML = postsAray[key-1].like

    setTimeout(() => {
       
        console.log("Delayed for 1 second.");
            zBlure.classList.remove('hidden')
    blure.classList.add('blur-sm')
    sBlure.classList.add('blur-sm')

      }, "500");
}
function setPostCunt() {
    console.log(postcount);
    postcount.innerHTML = postsAray.length
}



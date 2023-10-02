const  submitkey = document.getElementById('submitB')
const submiter =  document.getElementById('form')
 const myfile  = document.getElementById('myfile')
  const setProfile = document.getElementById('setProfile')









myfile.addEventListener('change',() => {
    const selectedFile = myfile.files[0];
    console.log(selectedFile.name);
    setProfile.src = `../${selectedFile.name}`
  }
)

submitkey.addEventListener('click', ()=>{
  submiter.submit()
 console.log(submiter.datafile.value)
})

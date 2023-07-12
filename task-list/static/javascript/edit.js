selectcolor=(colornumber)=>{
    let myDivObj=document.getElementsByClassName("color"+colornumber)[0]
    document.getElementById("color").value=window.getComputedStyle(myDivObj).backgroundColor
    console.log(window.getComputedStyle(myDivObj).backgroundColor)
}

const form = document.querySelector('form');
function submitForm(){
    form.submit()
}
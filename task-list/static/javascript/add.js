selectcolor=(colornumber)=>{
    let myDivObj=document.getElementsByClassName("color"+colornumber)[0]
    document.getElementById("color").value=window.getComputedStyle(myDivObj).backgroundColor
}

const form = document.querySelector('form');
function submitForm(){
    if(document.getElementById("color").value == ""){
        document.getElementById("color").value="rgb(255, 249, 221)"
    }
    form.submit()
}
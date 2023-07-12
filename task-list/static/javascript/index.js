clickbox=(number)=>{
    window.location.href="/details/"+number
}

color=(index, colornumber)=>{
    let myDivObj=document.getElementsByClassName("color"+colornumber)[0]
    if(colornumber == 1){
        console.log(index)
        console.log(colornumber)
        console.log(window.getComputedStyle(myDivObj).backgroundColor)
        window.location.href="/addcolor/"+index+"/"+colornumber
    }
    else if(colornumber == 2){
        console.log(index)
        console.log(colornumber)
        console.log(window.getComputedStyle(myDivObj).backgroundColor)
        window.location.href="/addcolor/"+index+"/"+colornumber
    }
    else if(colornumber == 3){
        console.log(index)
        console.log(colornumber)
        console.log(window.getComputedStyle(myDivObj).backgroundColor)
        window.location.href="/addcolor/"+index+"/"+colornumber
    }
    else{
        console.log(index)
        console.log(colornumber)
        console.log(window.getComputedStyle(myDivObj).backgroundColor)
        window.location.href="/addcolor/"+index+"/"+colornumber
    }
}

selected=(number)=>{
    window.location.href="/selectedColor/"+number
}

homepage=()=>{
    window.location.href="/"

}

checkedbox=(number, datanumber)=>{
    let box=document.getElementsByClassName("checkbox")[number - 1]
    if(box.checked){
        window.location.href="checkbox/1/"+datanumber
    }
    else{
        window.location.href="checkbox/0/"+datanumber
    }
}
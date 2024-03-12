window.addEventListener('load',function(){
    this.document.getElementById("os").selectedIndex =-1;
});

function Select(){
    let var_ = document.getElementById("os");
    //console.log(var_.selectedIndex); //returns the index of the selected choice
    //console.log(var_.value);  //returns the value of the first selected choice
    //refer jstutorial HTMLSelectElement and HTMLOptionElement
    if(var_.selectedIndex==-1){
        document.getElementById("1para").innerHTML = `You selected : None`;
    }
    else{
        document.getElementById("1para").innerHTML = `You selected : ${var_.options[var_.selectedIndex].text}`;
    }
}

function Add_option(){
    let Option_text = document.getElementById("choice").value;
    let Option_value = document.getElementById("os").options[document.getElementById("os").options.length-1].value;
    let newoption = new Option(Option_text,Option_value+1);
    let var_ = document.getElementById("os");
    var_.add(newoption,undefined);
    document.getElementById("os").selectedIndex = -1;
}

function Add_option_dom(){
    let new_option = document.createElement("option");
    let option_text = document.createTextNode(document.getElementById("choice").value);
    new_option.appendChild(option_text);
    document.getElementById("os").appendChild(new_option);
    document.getElementById("os").selectedIndex=-1;
}
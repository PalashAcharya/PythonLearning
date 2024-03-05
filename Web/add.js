function func(){
    let num1 = +document.getElementById("first_num").value;
    let num2 = +document.getElementById("second_num").value;
    document.getElementById("answer").value = num1+num2;
}

function reset(ids){
    ids.forEach(function(id) {
        document.getElementById(id).value=null;
    });
}

function eval(){
    let choice = document.getElementsByName('choice');
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    let num3 = +document.getElementById("num3").value;
    /*for(var i of choice){
        if(i.checked){
            var temp = i.value;
        }
    }*/
    for(var i=0;i<choice.length;i++){
        if(choice[i].checked){
            var temp = choice[i].value;
        }
    }
    console.log(temp);
    if(temp=='Max'){
        if(num1>num2){
            if(num1>num3){
                document.getElementById('ans').value=num1;
            }
            else{
                document.getElementById('ans').value=num3;
            }
        }
        else if(num2>num3){
            document.getElementById('ans').value=num2;
        }
        else{
            document.getElementById('ans').value=num3;
        }
    }
    else{
        if(num1<num2){
            if(num1<num3){
                document.getElementById('ans').value=num1;
            }
            else{
                document.getElementById('ans').value=num3;
            }
        }
        else if(num2<num3){
            document.getElementById('ans').value=num2;
        }
        else{
            document.getElementById('ans').value=num3;
        }

    }
    
}
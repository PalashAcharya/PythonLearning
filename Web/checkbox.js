function func(){
var list_ = document.getElementsByName('subjects');
var subject_list=[];
var answer_string ="You selected ";
for(var i of list_){
    if(i.checked){
        subject_list.push(i.value);
    }
}
for(var i of subject_list){
    answer_string += " "+i+","; 
}
document.getElementById('selected').value = answer_string;
}

function func2(){
   var listitems = document.getElementsByTagName('input');
   var answer_string = `You Selected: `;
   for(var i of listitems){
    if(i.checked){
        answer_string += ` ${i.value}`;
    }
   }
   document.getElementById('selected').value = answer_string;
}

function func3(){
    var string_ = `You Selected: `
    var check1 = document.getElementById('js');
    var check2 = document.getElementById('ds');
    var check3 = document.getElementById('db');
    if(check1.checked){
       string_ += ` ${check1.value}`; 
    }
    if(check2.checked){
        string_ += ` ${check2.value}`;
    }
    if(check3.checked){
        string_ += ` ${check3.value}`;
    }
    console.log(string_)
    document.getElementById('selected').value = string_;
}

function Checkall(){
    var listitems=document.getElementsByName('subjects');
    for(var i of listitems){
        i.checked=true;
    }
}

function Uncheckall(){
    var listitems = document.getElementsByName('subjects');
    for(var i of listitems){
        i.checked = false;
    }
}

function Invert(){
    var listitems = document.getElementsByName('subjects');
    for(var i of listitems){
        /*if(i.checked){
            i.checked = false;
        }
        else{
            i.checked = true;
        }*/
        i.checked=!i.checked;
    }
}
let toggle = true;
let iswin = false;
const win_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]];
const ev_ = new Event('click');
let count = [];
const button_ = [1,2,3,4,5,6,7,8,9];
let buttons = button_
function Func(ev){
    if(toggle){
        ev.target.value = "O";
        ev.target.disabled=true;
    }
    else{
        ev.target.value = "X";
        ev.target.disabled=true;
    }
    toggle= !toggle
    for(let i of win_combinations){
        if(document.getElementById(`button${i[0]}`).value=="O"&&document.getElementById(`button${i[1]}`).value=="O"&&document.getElementById(`button${i[2]}`).value=="O"){
            document.getElementById("win_statement").innerHTML="O wins";
            iswin = true;
        }
        else if(document.getElementById(`button${i[0]}`).value=="X"&&document.getElementById(`button${i[1]}`).value=="X"&&document.getElementById(`button${i[2]}`).value=="X"){
            document.getElementById("win_statement").innerHTML = "X wins";
            iswin = true;
        }
    }
    if(document.getElementById("button1").value!="" &&document.getElementById("button2").value!=""&&document.getElementById("button3").value!=""&&document.getElementById("button4").value!=""&&document.getElementById("button5").value!=""&&document.getElementById("button6").value!=""&&document.getElementById("button7").value!=""&&document.getElementById("button8").value!=""&&document.getElementById("button9").value!=""){
        if(iswin==false){
            document.getElementById("win_statement").innerHTML = "Draw";
        }
    }
    for(let i=1;i<=9;i++){
        if(document.getElementById(`button${i}`).value!=""){
            count.push(i);
        }
        else{
            continue;
        }
    }
    count = [...new Set(count)];
    buttons = buttons.filter(n=>!count.includes(n));
    computer_turn(ev);
}

function restart(){
    for(let i=1;i<=9;i++){
        if(document.getElementById(`button${i}`).value==""){
            continue;
        }
        else{
            document.getElementById(`button${i}`).value="";
            document.getElementById(`button${i}`).disabled=false;
        }
    }
    document.getElementById("win_statement").innerHTML = "";
    iswin = false;
    count.length = 0;
    buttons = button_;
}

function computer_turn(ev){
    if(count.length%2!=0){
        let random_num = Math.floor(Math.random()*buttons.length);
        if(ev.target.disabled){
            random_num = Math.floor(Math.random()*buttons.length);
            document.getElementById(`button${buttons[random_num]}`).dispatchEvent(ev_);
        }
        else{
            document.getElementById(`button${buttons[random_num]}`).dispatchEvent(ev_);
        }
    }
}
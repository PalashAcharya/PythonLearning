const text = document.getElementById("text1");
const button = document.getElementById("button1");
let value = "";
let dot_count = 0;
const len_ = {'count':''}
text.addEventListener('keydown',(event)=>{
    //keydown event is cancelable hence can use preventDefault() can be used
    if(event.cancelable){
        let key = event.key;
        const alpha_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVYXYZ';
        if(alpha_.includes(key)){
            event.preventDefault();
            alert("Please enter numeric values");
        }
        if(text.value.length>len_.count){
            event.preventDefault();
            alert("can only have two digits after point");
        }
    }
    else{
        alert("Cant cancel keydown event!");
    }
    if(event.key=="."){
        dot_count++;
        if(dot_count==1){
            len_.count = text.value.length+3;
            console.log(len_.count);
            console.log(text.value.length);
        }
        else{
            event.preventDefault();
            alert("Cant have two decimal points!");
        }
    }
})

button.addEventListener('click',(event)=>{
    console.log(event);
})

/*window.addEventListener('load',(ev)=>{
    //load is not cancelable
    if(ev.cancelable){
        alert("Event cancelled");
    }
    else{
        alert("Cant cancel load event!");
    }
})

/*document.body.addEventListener('keyup',(ev)=>{
    text.value=`you pressed ${ev.key}`;
})*/
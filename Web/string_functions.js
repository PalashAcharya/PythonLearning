let txt = "ThisIsAText";
document.getElementById('para').innerText=txt.length+" "+"length of the string";

let para_array = [];
para_array.push(document.createElement('p'));
para_array[0].innerHTML = txt.charAt(0)+" "+"character at specified index 0";
document.getElementById('divi').appendChild(para_array[0]);
para_array.push(document.createElement('p'));
para_array[1].innerHTML = txt.charCodeAt(4) +" "+"Unicode value of character at index 4";
document.getElementById('divi').appendChild(para_array[1]);

para_array.push(document.createElement('p'));
para_array.push(document.createElement('p'));

para_array[2].innerText = `${txt.at(2)} character found by at method`;
para_array[3].innerText = `${txt[2]} character found by indexing string`;
document.getElementById('divi').appendChild(para_array[2]);
document.getElementById('divi').appendChild(para_array[3]);

para_array.push(document.createElement('p'));
para_array[4].innerText = `${txt.slice(-7,-4)} used slice method to obtain isa`; //can use negative index
document.getElementById('divi').appendChild(para_array[4]);

para_array.push(document.createElement('p'));
para_array[5].innerText = `${txt.substring(4,7).toLowerCase()} used substring to obtain isa also used tolowercase`;//similar to slice but doesnt allow negative index and treats negative index as zero 
document.getElementById('divi').appendChild(para_array[5]);

para_array.push(document.createElement('p'));
para_array[6].innerText = `${txt.substr(4,3).toUpperCase()} obtained isa by substr method also used touppercase method`;//similar to slice and negative index possible but second parameter is the length of the substring
document.getElementById('divi').appendChild(para_array[6]);

let text1 = "Hello";
let text2 = "World";
console.log(text1.concat(" ",text2)); //all string methods are returning a new string and not modifying the original string as strings are immutable

text1 = "   Hello";
console.log(text1.trim()); //used to remove whitespace from both ends; use trimstart to remove from the start and trimend to remove from the end

console.log(text2.padStart(8,"0").padEnd(11,"x")); //make sure to consider the length of the string to pad
console.log(txt.replace(/text/i,"String")); //replace method replaces a string with another string; it is case sensitive so we use /i flag
console.log(txt.replace(/Text/g,'String')); //replace method also only replaces the first string so use the /g flag to remove all instances of the string to remove
console.log(txt.indexOf("Is"));
console.log(txt.lastIndexOf("Text")); //can use second parameter as starting index to search from that index in both indexof and lastindexof
console.log(txt.search("A")); //similar to indexof but cant take second parameter

let new_para = document.createElement('p');
new_para.innerText = "Final para";
document.body.append(new_para);
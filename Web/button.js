function func(id,num){
    document.getElementById(id).innerText = "A table is a structured set of data made up of rows and columns (tabular data). A table allows you to quickly and easily look up values that indicate some kind of connection between different types of data, for example a person and their age, or a day of the week, or the timetable for a local swimming pool.";
    document.getElementById(num).innerHTML="<a href='#'>Code</a>";
    let t1 = document.getElementById("input_text");
    console.log(t1.value)
}

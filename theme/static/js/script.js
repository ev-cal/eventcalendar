const burger = document.querySelector('#burger');
const menu = document.querySelector('#menu');

burger.addEventListener('click', () => {
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
    } else {
        menu.classList.add('hidden');
    }
})

var currentDate = new Date();

var year = currentDate.getFullYear();

var cp_year =currentDate.getFullYear();
var y = year;
document.getElementById("cpyear").value= cp_year
document.getElementById("year").value = year
document.getElementById("dv-year").innerHTML=year;

var day= currentDate.getDate();
document.getElementById("dv-day").innerHTML= day


var month = currentDate.getMonth();
if (month == 0) {
    document.getElementById("month").value = "January"
    document.getElementById("dv-month").innerHTML = "January"
}
else if (month == 1) {
    document.getElementById("month").value = "February"
    document.getElementById("dv-month").innerHTML = "February"
}
else if (month == 2) {
    document.getElementById("month").value = "March"
    document.getElementById("dv-month").innerHTML = "March"
}
else if (month == 3) {
    document.getElementById("month").value = "April"
    document.getElementById("dv-month").innerHTML = "April"
}
else if (month == 4) {
    document.getElementById("month").value = "May"
    document.getElementById("dv-month").innerHTML = "May"
}
else if (month == 5) {
    document.getElementById("month").value = "June"
    document.getElementById("dv-month").innerHTML = "June"
}
else if (month == 6) {
    document.getElementById("month").value = "July"
    document.getElementById("dv-month").innerHTML = "July"
}
else if (month == 7) {
    document.getElementById("month").value = "August"
    document.getElementById("dv-month").innerHTML = "August"
}
else if (month == 8) {
    document.getElementById("month").value = "September"
    document.getElementById("dv-month").innerHTML = "September"
}
else if (month == 9) {
    document.getElementById("month").value = "October"
    document.getElementById("dv-month").innerHTML = "October"
}
else if (month == 10) {
    document.getElementById("month").value = "November"
    document.getElementById("dv-month").innerHTML = "November"
}
else if (month == 11) {
    document.getElementById("month").value = "December"
    document.getElementById("dv-month").innerHTML = "December"
}


function next_month(){
    if(document.getElementById("month").value=="January"){
        document.getElementById("month").value="February"
    }else if(document.getElementById("month").value=="February"){
        document.getElementById("month").value="March"
        

    }else if(document.getElementById("month").value=="March"){
        document.getElementById("month").value="April"
        
    }else if(document.getElementById("month").value=="April"){
        document.getElementById("month").value="May"
        
    }else if(document.getElementById("month").value=="May"){
        document.getElementById("month").value="June"
        
    }else if(document.getElementById("month").value=="June"){
        document.getElementById("month").value="July"
        
    }else if(document.getElementById("month").value=="July"){
        document.getElementById("month").value="August"
        
    }else if(document.getElementById("month").value=="August"){
        document.getElementById("month").value="September"
        
    }else if(document.getElementById("month").value=="September"){
        document.getElementById("month").value="October"
        
    }else if(document.getElementById("month").value=="October"){
        document.getElementById("month").value="November"
        
    }else if(document.getElementById("month").value=="November"){
        document.getElementById("month").value="December"
        
    }else if(document.getElementById("month").value=="December"){
        document.getElementById("month").value="January"
    }
}








function prev_month(){
    if(document.getElementById("month").value=="January"){
        document.getElementById("month").value="December"
        
    }else if(document.getElementById("month").value=="February"){
        document.getElementById("month").value="January"
        
    }else if(document.getElementById("month").value=="March"){
        document.getElementById("month").value="February"
        
    }else if(document.getElementById("month").value=="April"){
        document.getElementById("month").value="March"
       
    }else if(document.getElementById("month").value=="May"){
        document.getElementById("month").value="April"
        
    }else if(document.getElementById("month").value=="June"){
        document.getElementById("month").value="May"
        
    }else if(document.getElementById("month").value=="July"){
        document.getElementById("month").value="June"
        
    }else if(document.getElementById("month").value=="August"){
        document.getElementById("month").value="July"
        
    }else if(document.getElementById("month").value=="September"){
        document.getElementById("month").value="August"
        
    }else if(document.getElementById("month").value=="October"){
        document.getElementById("month").value="September"
    }else if(document.getElementById("month").value=="November"){
        document.getElementById("month").value="October"
    }else if(document.getElementById("month").value=="December"){
        document.getElementById("month").value="November"

    }
}

function prev_year() {
    window.y = window.y - 1;
    document.getElementById("year").value = window.y
}

function next_year() {
    window.y = window.y + 1;
    document.getElementById("year").value = window.y
}

function monthClick(){
    const mv=document.querySelector('#mon-view');
    const dv=document.querySelector('#dai-view');
    const uv=document.querySelector('#upcoming');
    if(mv.classList.contains('hidden')){
        mv.classList.remove('hidden');
        dv.classList.add('hidden');
        uv.classList.add('hidden');
    }
}
function dailyClick(){
    const mv=document.querySelector('#mon-view');
    const dv=document.querySelector('#dai-view');
    const uv=document.querySelector('#upcoming');
    if(dv.classList.contains('hidden')){
        dv.classList.remove('hidden');
        mv.classList.add('hidden');
        uv.classList.add('hidden');
    }
}

function upcomingView(){
    const uv=document.querySelector('#upcoming')
    const mv=document.querySelector('#mon-view');
    const dv=document.querySelector('#dai-view');
    if(uv.classList.contains('hidden')){
        uv.classList.remove('hidden');
        mv.classList.add('hidden');
        dv.classList.add('hidden');
    }
}






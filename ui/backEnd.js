export const handleTimeButton = function(event) {
    let weekDays = " ";
    let M = document.getElementById('Mon').checked;
    let T = document.getElementById('Tue').checked;
    let W = document.getElementById('Wed').checked;
    let Th = document.getElementById('Thur').checked;
    let F = document.getElementById('Fri').checked;
    if(M){
        weekDays+="M ";
    }
    if(T){
        weekDays+="T ";
    }
    if(W){
        weekDays+="W ";
    }
    if(Th){
        weekDays+="Th ";
    }
    if(F){
        weekDays+="F ";
    }
    let update = document.getElementById('startTime').value + " - " + document.getElementById('endTime').value + " " + weekDays + " ";
    document.getElementById('timeUpdate').value += update;
}

export const handleCourseButton = function(event) {
    let update = document.getElementById('courseLabel').value + " " + document.getElementById('courseNumber').value + " ";
    document.getElementById('courseUpdate').value += update;
}

export const loadRequirements = function(){
    $("#timeButton").on( "click", handleTimeButton);

    $("#courseButton").on( "click", handleCourseButton);
}

$(function() {
    loadRequirements();
});


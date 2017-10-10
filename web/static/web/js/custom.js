$(function () {
    $('.datetime-input').datetimepicker({
        format:'DD-MM-YYYY HH:mm:ss'
    });
});

$(document).ready(function() {
    // page is now ready, initialize the calendar...
    $('#calendar').fullCalendar({
        // put your options and callbacks here
    })
});
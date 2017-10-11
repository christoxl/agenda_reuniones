$(function () {
    $('.datetime-input').datetimepicker({
        format: 'DD-MM-YYYY HH:mm:ss'
    });
});

$(document).ready(function () {
    $('#calendar').fullCalendar({
        events: '/api/'
    });
});
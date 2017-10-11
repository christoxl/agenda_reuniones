$(function () {
    $('.datetime-input').datetimepicker({
        format: 'DD-MM-YYYY HH:mm:ss'
    });
});

$(document).ready(function () {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay,listWeek'
        },
        defaultDate: '2017-10-12',
        navLinks: true, // can click day/week names to navigate views
        editable: true,
        eventLimit: true,
        events: '/api/'
    });
});
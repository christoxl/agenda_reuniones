$(function () {
    $('.datetime-input').datetimepicker({
        format:'DD-MM-YYYY HH:mm:ss'
    });
});

$(document).ready(function() {
    // page is now ready, initialize the calendar...
    $('#calendar').fullCalendar({
        header: {
            left: 'title',
            center: 'month,agendaWeek,agendaDay,listWeek'
        },
        navLinks: true,
        eventSources: [
            
                    // your event source
                    {
                        events: [ // put the array in the `events` property
                            {
                                title  : 'event1',
                                start  : '2017-10-12'
                            },
                            {
                                title  : 'event2',
                                start  : '2017-09-05'
                            },
                            {
                                title  : 'event3',
                                start  : '2010-01-09T12:30:00',
                            }
                        ],
                        color: 'black',     // an option!
                        textColor: 'yellow' // an option!
                    }
            
                    // any other event sources...
            
                ]
    })
});
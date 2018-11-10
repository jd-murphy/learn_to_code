$(document).ready(function(){
    
    console.log('javascript loaded from myjs.js');
    var lesson_number = $('#lesson_number').val();
    var next_lesson = (Number(lesson_number) + 1);
    var previous_lesson = (Number(lesson_number) - 1);
    
    $('#next_lesson_btn').each(function(){
        this.href += next_lesson
    });
    $('#previous_lesson_btn').each(function(){
        this.href += previous_lesson
    });

    $('#success_button').click(function(){
        console.log("sending ajax...");
        var csrftoken = Cookies.get('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                xhr.setRequestHeader("X-Frame-Options", undefined);
            }
        });
        $.ajax({
            method: 'POST',
            url: "http://localhost:8000/client_app/complete_lesson/",
            data: {
                "lesson_number": lesson_number
            }
        }).done(function() {
            $('.feedback_buttons').addClass('hide_me');
            $('#success_message').removeClass('hide_me');
            $('#help_message').addClass('hide_me');
            console.log('Lesson ' + lesson_number + ' marked as complete!')
        });
    });

    $('#help_button').click(function() {
        $('#help_message').removeClass('hide_me');
        $('#help_button').addClass('hide_me');
    });
})
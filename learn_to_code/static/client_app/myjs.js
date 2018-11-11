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

    var clipboard = new ClipboardJS('.copy-to-clip');

    $('.carousel').on('slide.bs.carousel',function(e){
        // var i = $(".active", e.target)[0];
        // var m = $('.' + i.id)[0];
        // $(m).removeClass("highlight-code");
        $(".highlight-code").each(function() {
            $(this).removeClass("highlight-code")
        })
        $('.' + e.relatedTarget.id).addClass("highlight-code")
      });
      

      $("#close-modal").click(function(){
          $('#next_lesson_btn').addClass('rubberBand')
      })

      effects = ["bounce", "flash", "pulse", "rubberBand", "shake", "swing", "tada", "wobble", "jello", "bounceIn", "bounceInDown", "bounceInLeft", "bounceInRight", "bounceInUp", "fadeIn", "fadeInDown", "fadeInDownBig", "fadeInLeft", "fadeInLeftBig", "fadeInRight", "fadeInRightBig", "fadeInUp", "fadeInUpBig", "flip", "flipInX", "flipInY", "lightSpeedIn", "rotateIn", "rotateInDownLeft", "rotateInDownRight", "rotateInUpLeft", "rotateInUpRight", "slideInUp", "slideInDown", "slideInLeft", "slideInRight", "zoomIn", "zoomInDown", "zoomInLeft", "zoomInRight", "zoomInUp", "jackInTheBox", "rollIn"]
      congrats_message = ["Great job, Coder!", "Keep it up, coder!", "Amazing work, coder!", "Nice! Stay focused, coder!", "Excellent work, coder!", "Great. Your skills are top notch!", "Great job! You're learning so much!", "Spot on. Keep it up, coder!", "#winning #awesomejob", "Very nice. Good work, coder.", "Great job. Keep up the momentum, coder!", "Nice work. You're doing great, coder.", "Really nice job. Keep on keepin' on, coder!", "I knew you would do great!", "Hard work pays off. You're learning so fast!", "Good stuff. Keep it up, coder!", "Amazing work, coder!", "Very nice. Keep up the hard work, coder.", "Awesome job out there!", "Top notch, coder! Good job!", "Nice skills, coder! Keep it up.", "You're doing great!", "Very nice. Good work!", "Awesome! Great work.", "Very nice. Stay focused.", "Your skills are improving!", "You make me proud coder!", "You're reallly getting the hang of this!", "Very nice. Proud of you!", "Good stuff. Very impressive.", "Excellent work.", "You've got what it takes!", "Impressive work again, coder.", "You're writing great code. Keep it up!", "Nice. Perserverance pays off!", "It's not easy, but you make it look easy!", "Great work.", "Wow! Your skills are impressive.", "You'll master python in no time.", "Your coding prowess is impressive. Nice job.", "What an accomplishment! Awesome work!", "Very nice! You're quite talented.", "Very nice work, coder. Very nice.", "Impressive work, coder!", "Great momentum. Stay on it! You're doing great!", "Top notch skills you've got there, coder!", "Excellent job, coder.", "Amazing work, coder."]
    
      next_effect = effects[Math.floor(Math.random()*effects.length)]
      next_message = congrats_message[Math.floor(Math.random()*congrats_message.length)]

      $("#unique-id > div").addClass(next_effect);
      $("#congrats-msg").text(next_message);
})
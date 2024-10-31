const monthNames = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June',
  'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
];
$("#comment-form").submit(function(e){
    e.preventDefault();
    console.log("button clicked.....");

    let dt = new Date();
    let time = dt.getDay() + "" + monthNames[dt.getUTCMonth()] + "," + dt.getFullYear()

    $.ajax({
          data: $(this).serialize(),
          method: $(this).attr("method"),
          url: $(this).attr("action"),
          dataType: 'json',

          success: function(res){
            console.log("comment save to DB....");

           if(res.bool == true){
           $(".review-res").html("Review added successfully..")
           $(".hide-comment-form").hide()

           let _html = '<li>'

               _html += '<div class="singel-reviews">'
               _html += '<div class="reviews-author">'
               _html += '<div class="author-thum">'
               _html += '<img src="" alt="Reviews">'
               _html += '</div>'
               _html += '<div class="author-name">'
               _html += '<h6>'+ res.context.user +'</h6>'
               _html += '<span>'+ time +'</span>'
               _html += '</div>'
               _html += '</div>'
               _html += '<div class="reviews-description pt-20">'
               _html += '<p>'+ res.context.review +'</p>'
               _html += '<div class="rating">'
               _html += '<ul>'
               for (let i = 1; i < res.context.rating; i++) {
                 _html += '<li><i class="fa fa-star"></i></li>'
               }

               _html += '</ul>'
               _html += '</div>'
               _html += '</div>'
               _html += '</div> <!-- singel reviews -->'
               _html += '</li>'
               $(".comment-list").prepend(_html)
           }
           }
        })
    })

$(".email-form").submit(function(e){
    e.preventDefault();
    console.log("button clicked.....");

      $.ajax({
          data: $(this).serialize(),
          method: $(this).attr("method"),
          url: $(this).attr("action"),
          dataType: 'json',

          success: function(res){
            console.log("comment save to DB....");
           $(".subscribe-success").html("Hello you have successfully sign up ..")
           $(".email-form").hide()

          }
     })
 })

 $(".address-form").submit(function(e){
    e.preventDefault();
    console.log("button clicked.....");

      $.ajax({
          data: $(this).serialize(),
          method: $(this).attr("method"),
          url: $(this).attr("action"),
          dataType: 'json',

          success: function(res){
            console.log("address save to DB....");
           $(".address-success").html("Hello you have successfully submitted your shipping address ..")
           $(".address-form").hide()

          }
     })
 })

$("#contactForm").submit(function(e){
    e.preventDefault();
    console.log("button clicked.....");

      $.ajax({
          data: $(this).serialize(),
          method: $(this).attr("method"),
          url: $(this).attr("action"),
          dataType: 'json',

          success: function(res){
            console.log("message save to DB....");
           $(".contact-success").html("Hello your message has been received..")
           $("#contactForm").hide()

          }
     })
 })

Fancybox.bind("[data-fancybox]", {
  // Your custom options
});


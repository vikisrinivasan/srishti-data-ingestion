(function ($) {
  $(document).ready(function () {
    generateID()
    choose()
    generateOption()
    selectionOption()
    removeClass()
    uploadImage()
    submit()
    resetButton()
    removeNotification()
    autoRemoveNotification()
    autoDequeue()

    var ID
    var way = 0
    var queue = []
    var fullStock = 10
    var speedCloseNoti = 1000
    var form_data = new FormData();
    var file_arr=[]
    var currentTab = 0; // Current tab is set to be the first tab (0)
    showTab(currentTab); // Display the current ta

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = 3

    setProgressBar(current);
    multiStepView()
    function multiStepView(){
    $(document).on("click",".next",function() {
    console.log("hi")
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    //Add Class Active
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;

    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    next_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(++current);
    });
    $(document).on("click",".previous",function() {

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //Remove class active
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

    //show the previous fieldset
    previous_fs.show();

    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;

    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    previous_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(--current);
    });
    }

    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    }

    $(".submit").click(function(){
    return false;
    })
    $(document).on("click","#mapping_save",function() {
                    original_cols=[]
                    mapped_cols=[]
                    var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
                    var type=$('.data_type').val();
                    var sheetname= $("fieldset:visible").find('#sheetname').val();
                    var filename= $("fieldset:visible").find('#filename').val();
                    var modeltype= $("fieldset:visible").find('#modeltype').val();
                     $("fieldset:visible").find(".mapping_table tr").each(function(){
                              original_cols.push($(this).find("td:nth-child(1)").text())
                              mapped_cols.push($(this).find(":selected").val())
                     })
                   $.ajax({
                             url: "save/",
                             method: "POST",
                             data: JSON.stringify({'type':type,'original_cols':original_cols,'mapped_cols':mapped_cols,'sheetname':sheetname,
                             'filename':filename,'modeltype':modeltype}),
                             contentType: "application/json",
                             dataType:"json",
                             headers:{'X-CSRFToken':csrf_token},
                             success: function (response) {
                                   alert('Data Saved')
                             }
                   })



            });
    function generateID() {
      var text = $('header span')
      var newID = ''

      for(var i = 0; i < 3; i++) {
        newID += Math.floor(Math.random() * 3)
      }

      ID = 'ID: 5988' + newID
      text.html(ID)
    }

    function choose() {
      var li = $('.ways li')
      var section = $('.sections section')
      var index = 0
      li.on('click', function () {
        index = $(this).index()
        $(this).addClass('active')
        $(this).siblings().removeClass('active')
        section.siblings().removeClass('active')
        section.eq(index).addClass('active')
        if(!way) {
          way = 1
        }  else {
          way = 0
        }
      })
    }

    function generateOption() {
      var select = $('select option')
      var selectAdd = $('.select-option .option')
      $.each(select, function (i, val) {
          $('.select-option .option').append('<div rel="'+ $(val).val() +'">'+ $(val).html() +'</div>')
      })
    }

    function selectionOption() {
      var select = $('.select-option .head')
      var option = $('.select-option .option div')

      select.on('click', function (event) {
        event.stopPropagation()
        $('.select-option').addClass('active')
      })

      option.on('click', function () {
        var value = $(this).attr('rel')
        $('.select-option').removeClass('active')
        select.html(value)

        $('select#datatype').val(value)
      })
    }

    function removeClass() {
      $('body').on('click', function () {
        $('.select-option').removeClass('active')
      })
    }

    function uploadImage() {
      var button = $('.images .pic')
      var uploader = $('<input type="file" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>')
      var images = $('.images')

      button.on('click', function () {
        uploader.click()
      })

      uploader.on('change', function () {
          var reader = new FileReader()
          reader.fileName = uploader[0].files[0].name
          reader.onload = function(event) {
            images.prepend('<div class="" style="background-color: #F5F7FA; text-align: center; padding: 40px 6px;text-transform: uppercase; color: black;font-size: 12px;cursor: pointer;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;width: 112px;margin-right: 12px;"><span>'+event.target.fileName+'</span></div>')
          }
          reader.readAsDataURL(uploader[0].files[0])
          form_data.append("title",$('#title').val())
          form_data.append('type',$('#datatype').val())
          form_data.append(reader.fileName,uploader[0].files[0])
      })

      images.on('click', '.img', function () {
        $(this).remove()
      })

    }

    function submit() {
      var button = $('#send')

      button.on('click', function () {

          var title = $('#title')
          var cate  = $('#datatype')
          var images = $('.images .img')
          var imageArr = []


          for(var i = 0; i < form_data.length; i++) {
            imageArr.push({file: form_data[i]})
          }
//          form_data.append('files',imageArr)
          sendData()
      })
    }

    function showTab(n) {
      // This function will display the specified tab of the form...
      var x = document.getElementsByClassName("wrapper");
      x[n].style.display = "block";

    }

    function nextPrev(n) {
          // This function will figure out which tab to display
          var x = document.getElementsByClassName("wrapper");
          // Exit the function if any field in the current tab is invalid:
          // Hide the current tab:
          x[currentTab].style.display = "none";
          // Increase or decrease the current tab by 1:
          currentTab = currentTab + n;

          // Otherwise, display the correct tab:
          showTab(currentTab);
    }

//    function mappingSave(){
//
//           console.log("hi");
//           $("#mapping_table tr").click(function(){
//                  $(this).find("td").each(function(){
//                       console.log($(this).html())
//                  });
//              });
////             $.ajax({
////                        url: "save/",
////                        method: "POST",
////                        data:  ,
////                        cache: false,
////                        processData: false,
////                        contentType: false,
////                        headers:{'X-CSRFToken':csrf_token},
////                        enctype: 'multipart/form-data',
////                        success: function (response) {
////                              $('#wrapper1').html(response);
////                              nextPrev(1)
////                        }
////                    })
//
//    }
 // <-- time in milliseconds
    function sendData(){
        console.log("hi")
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        setTimeout(function() {
            $('.alert-success').fadeOut('slow');
        },500000);
        $.ajax({
            url: "upload/",
            method: "POST",
            data: form_data,
            cache: false,
            processData: false,
            contentType: false,
            headers:{'X-CSRFToken':csrf_token},
            enctype: 'multipart/form-data',
            success: function (response) {
                  $('.alert-success').show()
                  $('.next').prop("disabled", false);
                  $('#msform').append(response);
                  steps = $("fieldset").length;
            }
        })

    }

    function removeNotification() {
      var close = $('.notification')
      close.on('click', 'span', function () {
        var parent = $(this).parent()
        parent.fadeOut(300)
        setTimeout(function() {
          parent.remove()
        }, 300)
      })
    }

    function autoRemoveNotification() {
      setInterval(function() {
        var notification = $('.notification')
        var notiPage = $(notification).children('.btn')
        var noti = $(notiPage[0])

        setTimeout(function () {
          setTimeout(function () {
           noti.remove()
          }, speedCloseNoti)
          noti.fadeOut(speedCloseNoti)
        }, speedCloseNoti)
      }, speedCloseNoti)
    }

    function autoDequeue() {
      var notification = $('.notification')
      var text

      setInterval(function () {

          if(queue.length > 0) {
            if(queue[0].type == 2) {
              text = ' Your discussion is sent'
            } else {
              text = ' Your order is allowed.'
            }

            notification.append('<div class="success btn"><p><strong>Success:</strong>'+ text +'</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
            queue.splice(0, 1)

          }
      }, 10000)
    }

    function resetButton() {
      var resetbtn = $('#reset')
      resetbtn.on('click', function () {
        reset()
      })
    }

    // helpers
    function saveToQueue(stock) {
      var notification = $('.notification')
      var check = 0

      if(queue.length <= fullStock) {
        if(stock.type == 2) {
            if(!stock.title || !stock.message) {
              check = 1
            }
        } else {
          if(!stock.title || !stock.datatype || stock.images == 0) {
            check = 1
          }
        }

        if(check) {
          notification.append('<div class="error btn"><p><strong>Error:</strong> Please fill in the form.</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
        } else {
          notification.append('<div class="success btn"><p><strong>Success:</strong> '+ ID +' is submitted.</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
          queue.push(stock)
          reset()
        }
      } else {
        notification.append('<div class="error btn"><p><strong>Error:</strong> Please waiting a queue.</p><span><i class=\"fa fa-times\" aria-hidden=\"true\"></i></span></div>')
      }
    }
    function reset() {

      $('#title').val('')
      $('.select-option .head').html('DataType')
      $('select#datatype').val('')

      var images = $('.images .img')
      for(var i = 0; i < images.length; i++) {
        $(images)[i].remove()
      }

      var topic = $('#topic').val('')
      var message = $('#msg').val('')
    }
  })
})(jQuery)
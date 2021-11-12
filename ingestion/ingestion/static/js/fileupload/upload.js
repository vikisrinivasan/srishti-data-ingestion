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
          form_data.append('file',uploader[0].files[0])

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


          sendData()


      })
    }

    function sendData(){
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
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
                console.log(response, typeof(response))
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
              text = ' Your discusstion is sent'
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
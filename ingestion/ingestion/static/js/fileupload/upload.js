(function($) {
    $(document).ready(function() {
        generateOption()
        selectionOption()
        removeClass()
        uploadData()
        submit()
        var form_data = new FormData();
        var file_arr = []
        var currentTab = 0; // Current tab is set to be the first tab (0)
        showTab(currentTab); // Display the current ta
        var current = 1;
        var steps = 3

        setProgressBar(current);
        multiStepView()

        function multiStepView() {
            $(document).on("click", ".next", function() {
                current_fs = $(this).parent();
                next_fs = $(this).parent().next();

                //Add Class Active
                $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

                //show the next fieldset
                next_fs.show();
                //hide the current fieldset with style
                current_fs.animate({
                    opacity: 0
                }, {
                    step: function(now) {
                        // for making fielset appear animation
                        opacity = 1 - now;

                        current_fs.css({
                            'display': 'none',
                            'position': 'relative'
                        });
                        next_fs.css({
                            'opacity': opacity
                        });
                    },
                    duration: 500
                });
                setProgressBar(++current);
            });
            $(document).on("click", ".previous", function() {

                current_fs = $(this).parent();
                previous_fs = $(this).parent().prev();

                //Remove class active
                $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

                //show the previous fieldset
                previous_fs.show();

                //hide the current fieldset with style
                current_fs.animate({
                    opacity: 0
                }, {
                    step: function(now) {
                        // for making fielset appear animation
                        opacity = 1 - now;

                        current_fs.css({
                            'display': 'none',
                            'position': 'relative'
                        });
                        previous_fs.css({
                            'opacity': opacity
                        });
                    },
                    duration: 500
                });
                setProgressBar(--current);
            });
        }

        function setProgressBar(curStep) {
            var percent = parseFloat(100 / steps) * curStep;
            percent = percent.toFixed();
            $(".progress-bar")
                .css("width", percent + "%")
        }

        // Generating Mapping table Between original Excel and Data Model
        $(document).on("click", '#generate_mapping', function() {
            var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            var sheetname = $('#mapping_sheetname_attr').val();
            var modeltype = $('#mapping_modeltype_attr').val();
            var filename = $('#mapping_filename_attr').val();
            $('.next').prop("disabled", true);
            $.ajax({
                url: "/render_mapping/",
                method: "POST",
                data: JSON.stringify({
                    'filename': filename,
                    'modeltype': modeltype,
                    'sheetname': sheetname
                }),
                contentType: "application/json",
                headers: {
                    'X-CSRFToken': csrf_token
                },
                success: function(response) {
                    $('.alert-success').text("Generated Data Mapping Successfully")
                    $('.alert-success').show()
                    $('.next').prop("disabled", false);
                    $(response).insertAfter('.mapping_selection_screen');
                    steps = $("fieldset").length;
                    $('.alert-success').fadeOut('slow');
                }
            })
        })

        // Saving of Final Mapping
        $(document).on("click", "#mapping_save", function() {
            original_cols = []
            mapped_cols = []
            var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            var modeltype = $("fieldset:visible").find('#modeltype').val();
            var sheetname = $("fieldset:visible").find('#sheetname').val();
            var filename = $("fieldset:visible").find('#filename').val();
            $("fieldset:visible").find(".mapping_table tr").each(function() {
                original_cols.push($(this).find("td:nth-child(1)").text())
                mapped_cols.push($(this).find(":selected").val())
            })
            $.ajax({
                url: "/save_mapping/",
                method: "POST",
                data: JSON.stringify({
                    'original_cols': original_cols,
                    'mapped_cols': mapped_cols,
                    'sheetname': sheetname,
                    'filename': filename,
                    'modeltype': modeltype
                }),
                contentType: "application/json",
                headers: {
                    'X-CSRFToken': csrf_token
                },
                success: function(response) {
                    if (response.includes("Error")) {
                        $('.alert-danger').text(response)
                        $('.alert-danger').show()
                    } else {
                        $('.alert-success').text(response)
                        $('.alert-success').show()
                    }
                    $('.alert-success').fadeOut(duration=1600);
                    $('.alert-danger').fadeOut(duration=40000);

                }
            })



        });
        // function for add button in file upload menu

        function generateOption() {
            var select = $('select option')
            var selectAdd = $('.select-option .option')
            $.each(select, function(i, val) {
                $('.select-option .option').append('<div rel="' + $(val).val() + '">' + $(val).html() + '</div>')
            })
        }

        function selectionOption() {
            var select = $('.select-option .head')
            var option = $('.select-option .option div')

            select.on('click', function(event) {
                event.stopPropagation()
                $('.select-option').addClass('active')
            })

            option.on('click', function() {
                var value = $(this).attr('rel')
                $('.select-option').removeClass('active')
                select.html(value)

                $('select#datatype').val(value)
            })
        }

        function removeClass() {
            $('body').on('click', function() {
                $('.select-option').removeClass('active')
            })
        }

        function uploadData() {
            var button = $('.images .pic')
            var uploader = $('<input type="file" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"/>')
            var images = $('.images .data_file_name')

            button.on('click', function() {
                uploader.click()
            })

            uploader.on('change', function() {
                var reader = new FileReader()
                reader.fileName = uploader[0].files[0].name
                reader.onload = function(event) {
                    images.html('<div class="" style="background-color: #F5F7FA; text-align: center; padding: 40px 6px;text-transform: uppercase; color: black;font-size: 12px;cursor: pointer;text-overflow: ellipsis;white-space: nowrap;overflow: hidden;width: 112px;margin-right: 12px;"><span>' + event.target.fileName + '</span></div>')
                }
                reader.readAsDataURL(uploader[0].files[0])
                form_data=new FormData()
                form_data.append('type', $('#datatype').val())
                form_data.append(reader.fileName, uploader[0].files[0])
            })


        }

        // function for triggering sendData to save the uploaded file data to interim location which is /data/
        function submit() {
            var button = $('#send')

            button.on('click', function() {

                var title = $('#title')
                var cate = $('#datatype')
                var images = $('.images .img')
                var imageArr = []


//                for (var i = 0; i < form_data.length; i++) {
//                    imageArr.push({
//                        file: form_data[i]
//                    })
//                }
//                alert(length)
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

        function sendData() {
            csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
            $('#load-saving').show();
            $('#send').prop('disabled',true);
            $.ajax({
                url: "/upload_file/",
                method: "POST",
                data: form_data,
//                cache: false,
                processData: false,
                contentType: false,
                headers: {
                    'X-CSRFToken': csrf_token
                },
                enctype: 'multipart/form-data',
                success: function(response) {
                    $('.alert-success').text("Data Saved Successfully")
                    $('.alert-success').show()
                    $('#load-saving').hide()
                    $('.next').prop("disabled", false);
                    $('#send').prop('disabled',false);
                    $('#msform fieldset:nth-child(2)').remove()
                    $('#msform').append(response);
                    steps = $("fieldset").length;
                    $('.alert-success').fadeOut('slow');
                }
            })

        }




    })
})(jQuery)
//Variable current output
var outputName = '';

$(document).ready(function () {
    // Init
    $('.process-section').hide();
    $('.loader').hide();
    $('#result').text('');
    $('.freeText-section').hide();

    // $('#result').hide();
    // $('.btn-predict').hide();

    // Upload Preview
    function readURL(fileInput) {
        // if (input.files && input.files[0]) {
        //     var reader = new FileReader();
        //     reader.onload = function (e) {
        //         $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
        //         $('#imagePreview').hide();
        //         $('#imagePreview').fadeIn(650);
        //     }
        //     reader.readAsDataURL(input.files[0]);
        // }
        console.log(fileInput.files[0])
        var files = fileInput.files;

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            var imageType = /image.*/;

            if (!file.type.match(imageType)) {
              continue;
            }
            var img = document.getElementById("thumbnail");
            img.file = file;
            var reader = new FileReader();
            reader.onload = (function(aImg) {
              return function(e) {
                aImg.src = e.target.result;
              };
            })(img);
            reader.readAsDataURL(file);
        }
    }

    $("#imageUpload").change(function () {
        // $('.image-section').show();
        // $('#btn-predict').show();
        $('#result').text('');
        // $('#result').hide();
        $('.download-section').hide();
        $('.process-section').show();
        $('.image-preview').show();
        $('.output-preview').hide();
        readURL(this);
    });


    // $('#login-status').text(function(i, oldText) {
    //     if (oldText != 'null'){
    //         $('.freeText-section').hide();
    //     }
    // });

    // Download
    $('#btn-download').click(function () {
        var a = $("<a>")
              .attr("href", "/static/outputs/" + outputName)
              .attr("download", outputName)
              .appendTo("body");

        a[0].click();
        a.remove();
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        // $(this).hide();
        $('.process-section').hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function(data) {
                // Get and display the result
                $('.loader').hide();
                $('.output-preview').show();
                // $('#result').fadeIn(600);
                // $('#result').text(' Result:  ' + data);

                var statusOrder = $("#login-status").text();
                console.log('statusOrder: ' + statusOrder);

                if (statusOrder != 'null'){
                    $('.download-section').show();
                    $('.upload-section').show();
                    $('.freeText-section').hide();
                } else {
                    $('.download-section').hide();
                    $('.upload-section').hide();
                    $('.freeText-section').show();
                }

                $('#result').fadeIn(600);
                $('#result').text(data);

                console.log('Status: Success Ok! ' + data);
            },
        });
    });
});

//function for displaying the image upload preview
function showMyImage(fileInput) {
  console.log("showMyImage-----------------------------")
  $('.download-section').hide();
  $('.process-section').show();
  $('.image-preview').show();
  $('.output-preview').hide();

  var files = fileInput.files;

  for (var i = 0; i < files.length; i++) {
      var file = files[i];
      var imageType = /image.*/;

      if (!file.type.match(imageType)) {
        continue;
      }
      var img = document.getElementById("thumbnail");
      img.file = file;
      var reader = new FileReader();
      reader.onload = (function(aImg) {
        return function(e) {
          aImg.src = e.target.result;
        };
      })(img);
      reader.readAsDataURL(file);
  }
};

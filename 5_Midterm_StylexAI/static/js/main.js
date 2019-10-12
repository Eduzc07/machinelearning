//Variable current output
var outputName = '';

$(document).ready(function () {
    // Init
    $('.process-section').hide();
    $('.loader').hide();

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
        // $('#result').text('');
        // $('#result').hide();
        $('.download-section').hide();
        $('.process-section').show();
        $('.image-preview').show();
        $('.output-preview').hide();
        readURL(this);
    });


    $('#login-status').text(function(i, oldText) {
        if (oldText != 'null'){
            $('.freeText-section').hide();
        }
    });

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
            success: function(nameFile) {
                // Get and display the result
                $('.loader').hide();
                $('.output-preview').show();
                // $('#result').fadeIn(600);
                // $('#result').text(' Result:  ' + data);

                var statusOrder = $("#login-status").text();
                console.log('statusOrder: ' + statusOrder);

                if (statusOrder != 'null'){
                    $('.download-section').show();
                } else {
                    $('.download-section').hide();
                }

                outputName = nameFile;
                console.log('Status: Success Ok! ' + nameFile);
                // document.getElementById('outputImage').src = '~/static/outputs/output.png'
                // $('#outputImage').src("<img  src="{{ url_for('static', filename='outputs/output.png')}}"/>");
                $("#outputImage").attr("src", "/static/outputs/" + nameFile);
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

function styleFunction(object) {
  $('.output-preview').hide();
  // $('.image-preview').hide();


  if($('.image-preview').is(":visible")){
    $('.process-section').show();
  }


  $('.download-section').hide();

  var name = ''
  switch(object.selectedIndex) {
    case 0:
      name = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
      break;
    case 1:
      name = "https://upload.wikimedia.org/wikipedia/en/3/38/Gino_Severini%2C_1912%2C_Dynamic_Hieroglyphic_of_the_Bal_Tabarin%2C_oil_on_canvas_with_sequins%2C_161.6_x_156.2_cm_%2863.6_x_61.5_in.%29%2C_Museum_of_Modern_Art%2C_New_York.jpg"
      break;
    case 2:
      name = "https://www.wallpaperup.com/uploads/wallpapers/2015/04/08/658128/6dce3e6d31eff2996064a7a2334b906f.jpg"
      break;
    case 3:
      name = "https://i.pinimg.com/originals/a5/6b/c3/a56bc3bd1f6fe8150e2931de7e3c7544.jpg"
      break;
    case 4:
      name = "https://lamula.pe/media/uploads/583b98da-5312-46f1-b284-3e0cd6a9507a.jpg"
      break;
    case 5:
      name = "https://cdn3.vectorstock.com/i/1000x1000/52/17/selfie-pop-art-style-vector-8685217.jpg"
      break;
    case 6:
      name = "https://i2.wp.com/painterlegend.com/wp-content/uploads/images/leonid-afremov-wallpapers-wallpaper-cave-greatest-artwork-ever.jpg?fit=800%2C500&ssl=1"
      break;
    case 7:
      name = "https://theculturetrip.com/wp-content/uploads/2017/03/rexfeatures_5850811in.jpg"
      break;
    case 8:
      name = "https://www.liveabout.com/thmb/HdzAVnTU2XLkxj5tNlk13QEU4_8=/2835x1890/filters:fill(auto,1)/Mona_Lisa-copy-56a6e6d95f9b58b7d0e56987.jpg"
      break;
    case 9:
      name = "https://www.redsharknews.com/media/k2/items/src/242b7cac26b02f080edc3ea8e0e494ba.jpg"
      break;
    default:
      name = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
  }

  document.getElementById('style-image').src = name

  $.ajax({
      type: "POST",
      url: "/style",
      data: name,
      contentType: false,
      cache: false,
      processData: false,
      async: true
  });
};

function iterFunction(object) {
    var iteration = object.options[object.selectedIndex].value
    console.log('iter: '+ iteration)
    $.ajax({
        type: "POST",
        url: "/iteration",
        data: iteration,
        contentType: false,
        cache: false,
        processData: false,
        async: true
    });
};

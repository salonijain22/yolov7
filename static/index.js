window.onload = () => {
  $("#sendbutton").click(() => {
    imagebox = $("#imagebox");
    link = $("#link");
    input = $("#imageinput")[0];
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("video", input.files[0]);
      $.ajax({
        url: "/detect", // fix this to your liking
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          console.log(data);
          $("#link").css("visibility", "visible");
          $("#download").attr("href", data);
          console.log(data);
        // $.get("/").done(function (data) {
        //   $("#imagebox").attr("src", data);
        //   console.log("sucesssss", data);
        // })
        },
      });
    }
  });
  // $("#download").click(() => {
  //   console.log("click");
  //   // fetch('/download')
  //   //   .then(response => {
  //   //       console.log(response);
  //   //   })
  //   //   .then(data=>{
  //   //     console.log(data);
  //   //     $("#res").text(data)
  //   //   })
  //   //   .catch(error => {
  //   //     console.log(error);
  //   //   })
  //   // $("#res").text(data)
  //   var datastring = $(this).serialize(); 
  //   console.log(datastring)
  //   $.ajax({
  //     url:"/detect",
  //     type:"POST",
  //     // dataType:"text",
  //     error: function () {
  //       console.log("download error");
  //     },
  //     success: function (data) {
  //       console.log("data");
  //       $("#res").text(data)
  //     }
  //   })
  // })
  $("#opencam").click(() => {
    console.log("evoked openCam");
    $.ajax({
      url: "/opencam",
      type: "GET",
      error: function (data) {
        console.log("upload error", data);
      },
      success: function (data) {
        console.log(data);
      }
    });
  })
};

function readUrl(input) {
  imagebox = $("#imagebox");
  console.log(imagebox);
  console.log("evoked readUrl");
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      console.log(e.target);

      imagebox.attr("src", e.target.result);
        imagebox.height(500);
        imagebox.width(800);
    };
    reader.readAsDataURL(input.files[0]);
  }
}


function openCam(e){
  console.log("evoked openCam");
  e.preventDefault();
  console.log("evoked openCam");
  console.log(e);
}
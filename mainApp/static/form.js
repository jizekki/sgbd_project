

$("#addNewClubButton").click(function () {
  $("#formInformationsFields").toggle('.hiddenBlock');

});


$('input[type="checkbox"]').each(function () {
  $(this).prop('checked', false);
});


$('input[type="checkbox"]').click(function () {
  if ($('input[type="checkbox"]:checked').length == $('input[type="checkbox"]').length) {
    $("#submitForm").removeClass('disabled');
  }
  else {
    $("#submitForm").addClass('disabled');
  }
});


function submit_form() {
  var url = `/form_submitted`;
  var dataString = '&firstName=' + $('input[name=firstName]').val() +
    '&lastName=' + $('input[name=lastName]').val() +
    '&subscription=' + $('input[name=subscription]').val() +
    '&email=' + $('input[name=email]').val() +
    '&phoneNumber=' + $('input[name=phoneNumber]').val() +
    '&birthdate=' + $('input[name=birthdate]').val();
  var subsc = $('input[name=subscription]').val();
  if (subsc == "0") {
    alert('ERROR');
  };
  $.ajax({
    url: url,
    type: "POST",
    csrfmiddlewaretoken: '{{ csrf_token }}',
    data: dataString,
    beforeSend: function () {
      console.log(subsc);
      if (subsc == "0") {
        ajaxReq.abort();
      }
    },
    success: function (json) {
      alert(success);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      alert(errorThrown);
    }
  });

};

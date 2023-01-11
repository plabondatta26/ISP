$("#service_form").submit(function (e) {
  e.preventDefault();

  let status = false;
  for (var i = 0; i < $(this).find('input[name="service"]').length; i++) {
    if ($(this).find('input[name="service"]')[i].checked === false) {
      if (status != true) {
        console.log("wrong");
        status = false;
      }
    } else {
      console.log("ok1");
      status = true;
    }
  }
  if (status === true) {
    $("#service_form").submit();
  } else {
    alert("Please select at least one from given item");
    return false;
  }
});

$("#package_form").submit(function (e) {
  e.preventDefault();

  let status = false;

  const radioButtons = document.querySelectorAll('input[name="package"]');
  for (const radioButton of radioButtons) {
    console.log(radioButton);
    if (radioButton.checked) {
      selectedSize = radioButton.value;
      status = true;
      if (status != true) {
        status = false;
      }
    } else {
      status = false;
    }
  }

  if (status === true) {
    $("#package_form").submit();
  } else {
    alert("Please select at least one from given item");
    return false;
  }
});

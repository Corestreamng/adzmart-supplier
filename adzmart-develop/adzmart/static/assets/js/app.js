$(document).on("click", "#load-staffs", function () {
  window.location.replace("/staffs/");
});
$(document).on("click", "#load-billboard-catalog", function () {
  window.location.replace("/catalog/billboard");
});
$(document).on("click", "#load-radio-catalog", function () {
  window.location.replace("/catalog/radio");
});
$(document).on("click", "#load-tv-catalog", function () {
  window.location.replace("/catalog/tv");
});
$(document).on("click", "#load-cinema-catalog", function () {
  window.location.replace("/catalog/cinema");
});
$(document).on("click", "#load-print-catalog", function () {
  window.location.replace("/catalog/print");
});
$(document).on("click", "#load-special-offer", function () {
  window.location.replace("/catalog/special-offers");
});

function copyText($) {
  var copyText = document.getElementById($.dataset.descRef);
  copyText.select();
  copyText.setSelectionRange(0, 99999); // For mobile devices
  navigator.clipboard
    .writeText(copyText.value)
    .then(() => alert("Invitation Link copied to clipboard"))
    .catch(() => "Something went wrong!");
}

$(document).ready(function () {
  $(".toggle-element").click(function () {
    if ($(this).hasClass("active")) {
      $(this).removeClass("active");
    } else {
      $(".toggle-element").removeClass("active");
      $(this).addClass("active");
    }
  });
});

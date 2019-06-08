app = {};
app.setEvents = function() {
  $(".generate-sidebar").on("click", function(e) {
    $(".content .ui.section").hide();
    $(".content .ui.generate.section").show();
    $(this)
      .parent(".sidebar")
      .find(".active")
      .removeClass("active teal");
    $(this).addClass("active teal");
  });
  $(".settings-sidebar").on("click", function(e) {
    $(".content .ui.section").hide();
    $(".content .ui.settings.section").show();
    $(this)
      .parent(".sidebar")
      .find(".active")
      .removeClass("active teal");
    $(this).addClass("active teal");
  });
};

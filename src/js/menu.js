(function($) {
  $(".openbtn").on("click", function() {
    console.info("click in openbtn");
    $(".ui.sidebar").toggleClass("very thin icon");
    $(".asd").toggleClass("marginlefting");
    $(".sidebar z").toggleClass("displaynone");
    $(".ui.accordion").toggleClass("displaynone");
    $(".ui.dropdown.item").toggleClass("displayblock");

    $(".logo")
      .find("img")
      .toggle();
  });
  $(".ui.dropdown").dropdown({
    allowCategorySelection: true,
    transition: "fade up",
    context: "sidebar",
    on: "hover"
  });

  $(".ui.accordion").accordion({
    selector: {}
  });
})(jQuery);

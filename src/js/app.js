var {
  PythonShell
} = require("python-shell");
var path = require("path");
app = {};
app.setEvents = function () {
  $(".generate-sidebar").on("click", function (e) {
    $(".content .ui.section").hide();
    $(".content .ui.generate.section").show();
    $(this).parent(".sidebar").find(".active").removeClass("active teal");
    $(this).addClass("active teal");
  });
  $(".settings-sidebar").on("click", function (e) {
    $(".content .ui.section").hide();
    $(".content .ui.settings.section").show();
    $(this).parent(".sidebar").find(".active").removeClass("active teal");
    $(this).addClass("active teal");
  });
};
app.Hi = function () {
  let name = $("#txtName").val();
  let options = {
    scriptPath: path.join(__dirname, "/src/engine/"),
    args: [name]
  };
  var hi = new PythonShell('hello.py', options);
  hi.on('message', function (message) {
    $("#lblName").text(message);
  });
}
// Generated by CoffeeScript 1.10.0
var check_counters_buttons, check_is_speaker, set_active_navbar;

jQuery(function() {
  set_active_navbar();
  check_is_speaker();
  check_counters_buttons("#num-speakers", "#btn-show-speakers");
  check_counters_buttons("#num-listeners", "#btn-show-listeners");
  return $("#id_is_speaker").on("click", check_is_speaker);
});

set_active_navbar = function() {
  return $(".nav li").each(function(i, obj) {
    var current_href, li, li_href, potencial_dropdown;
    li = $(this);
    li.removeClass("active");
    li_href = li.find("a").attr("href");
    current_href = window.location.pathname;
    if (li_href === current_href) {
      potencial_dropdown = li.parent().parent();
      if (potencial_dropdown.hasClass("dropdown")) {
        console.log("hola");
        potencial_dropdown.addClass("active");
      }
      return li.addClass("active");
    }
  });
};

check_is_speaker = function() {
  var text;
  if ($("#id_is_speaker").prop("checked")) {
    text = "Continuar a formulario de ponente";
  } else {
    text = "Enviar";
  }
  return $("#btn-register").text(text);
};

check_counters_buttons = function(counter, button) {
  if ($("" + counter).text() === "0") {
    return $("" + button).addClass("disabled");
  } else {
    return $("" + button).removeClass("disabled");
  }
};

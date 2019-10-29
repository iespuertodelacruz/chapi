jQuery ->
    set_active_navbar()
    check_is_speaker()
    check_counters_buttons("#num-speakers", "#btn-show-speakers")
    check_counters_buttons("#num-listeners", "#btn-show-listeners")
    $("#id_is_speaker").on("click", check_is_speaker)

set_active_navbar = ->
    $(".nav li").each (i, obj) ->
        li = $(@)
        li.removeClass("active")
        li_href = li.find("a").attr("href")
        current_href = window.location.pathname
        if li_href == current_href
            potencial_dropdown = li.parent().parent()
            if potencial_dropdown.hasClass("dropdown")
                console.log("hola")
                potencial_dropdown.addClass("active")
            li.addClass("active")

check_is_speaker = ->
    if $("#id_is_speaker").prop("checked")
        text = "Continuar a formulario de ponente"
    else
        text = "Enviar"
    $("#btn-register").text(text)

check_counters_buttons = (counter, button) ->
    if $("#{counter}").text() == "0"
        $("#{button}").addClass("disabled")
    else
        $("#{button}").removeClass("disabled")

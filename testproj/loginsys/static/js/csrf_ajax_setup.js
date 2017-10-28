function get_csrf_token(){
    return jQuery("[name=csrfmiddlewaretoken]").val();
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function csrf_token_setup(){
    console.log("csrf token setup start...");
    csrftoken = get_csrf_token();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    console.log("csrf token setup was completed.");
}

csrf_token_setup()
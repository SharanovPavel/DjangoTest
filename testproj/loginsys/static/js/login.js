function login_form_ajax_submit_setup() {
    console.log("login form setup start...");
    var frm = $('#loginForm');
        frm.submit(function (e) {    
        e.preventDefault();
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                if(data.success){
                    console.log('Logged in');
                    window.location = "/";
                }
                else{
                    alert('Fail!')
                }
            }});
        });
    console.log("login form setup was completed.");
}

login_form_ajax_submit_setup();

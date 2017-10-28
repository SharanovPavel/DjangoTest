function register_form_ajax_submit_setup() {
    console.log("login form setup start...");
    var frm = $('#registerForm');
        frm.submit(function (e) {    
        e.preventDefault();
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                console.log('Submission was successful.');
                if(data.success){
                    alert('Registered successfuly! Please, log in!');
                    window.location = "/auth/login";
                }
                else{
                    alert('Failed! Try again!')
                }
            },
            error: function (data) {
                console.log('An error occurred.');
            },
            });
        });
    console.log("login form setup was completed.");
}

register_form_ajax_submit_setup()

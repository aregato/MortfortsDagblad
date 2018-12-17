$(document).ready(function(){
  $('#show_password').on('click', function(){

    var passwordField = $('#psw');

    var passwordFieldType = passwordField.attr('type');

    if(passwordFieldType == 'password')
    {

        passwordField.attr('type', 'text');

        $(this).val('Dölj lösenordet');
    } else {

        passwordField.attr('type', 'password');

        $(this).val('Visa lösenordet');
    }
  });
  });

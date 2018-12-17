function checkForm(form)
{

re = /^\w+$/;
if(!re.test(form.username.value)) {
  alert("Användarnamn får bara innehålla bokstäver och siffror");
  form.username.focus();
  return false;

}

if(form.psw.value.length < 6) {
  alert("Lösenordet måste vara längre än 6 karaktärer");
  form.psw.focus();
  return false;
}
if(form.psw.value == form.username.value) {
  alert("Lösenordet måste vara annorlunda från användarnamnet");
  form.psw.focus();
  return false;
}
re = /[0-9]/;
if(!re.test(form.psw.value)) {
  alert("Lösenordet måste innehålla minst en siffra");
  form.psw.focus();
  return false;
}

}

$(function(){

  $( "#ArticleButton" ).click(function(){addArticles();});

  $( "#addForfButton" ).click(function(){addForfs();});
  $("#bildButton").click(function(){addBild();});

  $( "#kopplaForf" ).click(function(){connectForf();});
  $( "#kopplaBild" ).click(function(){connectBild();});

});




function addArticles(){
  let rubrik = $('#rubrik').val();
  let ingress = $('#ingress').val();
  let text = $('#text').val();
  let date = $('#date').val();

  if(rubrik == ""){
    console.log("Rubrik saknas");
  }else if(ingress == ""){
    console.log("Ingress saknas");
  }else if(text == ""){
    console.log("Text saknas");
  }else if(date == ""){
    console.log("Datum saknas");
  }else{
    $("#addArtModel").modal();
  }
};

function addForfs(){
  let namn = $('#namn').val();
  let efternamn = $('#efternamn').val();
  let email = $('#email').val();
  let telefon = $('#telefon').val();
  let losenord = $('#losenord').val();

  if(namn == ""){
    console.log("Namn saknas");
  }else if(efternamn == ""){
    console.log("Efternamn saknas");
  }else if(email == ""){
    console.log("Email saknas");
  }else if(telefon == ""){
    console.log("Telefon saknas");
  }else if(losenord == ""){
    console.log("Lösenord saknas");
  }else{
    console.log("Lägg till:", email);
    $("#addForfModel").modal();
  }
};

function addBild(){
  let namn = $("#bildnamn").val();
  let bild = $("#bild").val();
  if(namn == ""){
    console.log("Namn saknas");
  }else if(bild == ""){
    console.log("Efternamn saknas");
  }else{
    console.log("Lägger till bild")
    $("#addBildModel").modal();
  }
}

function connectForf(){
  let af = $("#artforf").val();
  let fa = $("#forfart").val();
  if(af == null){
    console.log("Saknar artikel koppling")
  }else if(fa == null){
    console.log("Saknar forfattar koppling")
  }else{
    console.log(af, fa);
    $("#connectForfModel").modal();
  }
};

function connectBild(){
  let ab = $("#artbild").val();
  let ba = $("#bildart").val();

  if(ab == null){
    console.log("Saknar artikel koppling")
  }else if(ba == null){
    console.log("Saknar bild koppling")
  }else{
    console.log(ab, ba);
    $("#connectBildModel").modal();
  }
};

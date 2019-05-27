$(function(){
    $( "#commentaryButton" ).click(function(){addCommentary();});
});

function addCommentary(){
  let knamn = $('#knamn').val();
  let kommentar = $('#kommentar').val();
  if(knamn == ""){
    console.log("Namn saknas");
  }else if(kommentar == ""){
    console.log("Efternamn saknas");
  }else{
    console.log("Lägg till:", knamn);
    $("#addCommentaryModel").modal();
  }
};

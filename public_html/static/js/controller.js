/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(function(){
    check_logged_in() 
    $(".tight").click(function(){if_logout()});
});

function check_logged_in(){  
    var logged_user = localStorage.getItem('user');
    
    console.log(logged_user);
    
    if(logged_user == "undefined"){
        console.log("LocalStorage är tomt.");
        if_logout();
    }else if(logged_user == null){
        console.log("LocalStorage är null.");
        if_logout();
    }else{
        console.log("Inloggad som: " + logged_user);
        if_logged_in();
    }
}

function if_logged_in(){
    console.log("Loggar in");

    $("#footerIn").hide()
    $("#footerOut").show()
}
function if_logout(){
    console.log("Loggar ut");
    
    localStorage.removeItem('user');
    $("#footerIn").show()
    $("#footerOut").hide()
}
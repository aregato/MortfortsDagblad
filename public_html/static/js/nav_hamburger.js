/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(function(){
    $("#hamburger").click(function(){
        var logged_user = localStorage.getItem('user');
        
        if(logged_user == "undefined"){
            
            showMenu();
            
        }else if(logged_user == null){
            
            showMenu();
            
        }else{
            console.log("Inloggad som: " + logged_user);
            showLoggedMenu();
        }
        
    }); 
});


function showMenu(){
    
    var className = $('#hamburger').attr('class');
    if(className === "hamburger hamburger--collapse"){
        console.log(className);
        $("#hamburger").addClass("is-active");
        
        $("#menu").fadeIn(500); 
    }else{
        $("#hamburger").removeClass("is-active");
        
        $("#menu").fadeOut(200);
    }
}
function showLoggedMenu(){
    var className = $('#hamburger').attr('class');
    if(className === "hamburger hamburger--collapse"){
        console.log(className);
        $("#hamburger").addClass("is-active");
        
        $("#logInMenu").fadeIn(500); 
    }else{
        $("#hamburger").removeClass("is-active");
        
        $("#logInMenu").fadeOut(200);
    }
}
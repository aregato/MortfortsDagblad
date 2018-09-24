/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(function(){
    console.log("Starta");
    logIn();
});

function logIn(){  
    var user = $('.username').html();
    localStorage.setItem('user', user);
    console.log("Loggar in:" + user);
}



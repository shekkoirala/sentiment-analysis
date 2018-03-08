
// JavaScript Document
"use strict";

//Global Variable Declaration

function update(){
	//Event Handlers and listeners
	
	document.getElementById("technology").onclick = function(){
        
		document.getElementById("content").data="technology.html";
		
    };
    document.getElementById("home").onclick=function(){
        
        document.getElementById("content").data="home.html";
    };
    document.getElementById("categories").onclick=function(){
        
        document.getElementById("content").data="categories.html";
    };
    document.getElementById("searchresults").onclick=function(){
        
        document.getElementById("content").data="searchresults.html";
    };
    document.getElementById('search').addEventListener('keypress', function(event) {
        if (event.keyCode == 13) {
            
        }
    });
	
}

window.onload = function() {
	// prep anything we need to
    document.getElementById("content").data="home.html";
		setInterval(update,1000);
	
};
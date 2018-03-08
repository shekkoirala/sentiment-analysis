// JavaScript Document
"use strict";

//Global Variable Declaration


function update(){
	//Event Handlers and listeners
	
	document.getElementById("searchbtn").onclick = function(){
		
		
    };
    document.getElementById('search').addEventListener('keypress', function(event) {
        if (event.keyCode == 13) {
            
        }
    });
	
}

window.onload = function() {
	// prep anything we need to
	
		setInterval(update,1000);
	
};
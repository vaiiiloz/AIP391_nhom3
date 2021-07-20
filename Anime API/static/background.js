// JavaScript source code

var menuItem = {
	"id":"Anime",
	"title":"Anime",
	"contexts":["image"]
};



var xhr = new XMLHttpRequest();
chrome.contextMenus.create(menuItem);
//const yourURL = 'http://127.0.0.1:5000'
const yourURL = "/API"
chrome.contextMenus.onClicked.addListener(function(clickData){
	if (clickData.menuItemId == "Anime"){
	
	
		xhr.open("POST", yourURL, true);
		xhr.setRequestHeader('Content-Type', 'application/json');
		xhr.send(JSON.stringify({
			value: clickData.srcUrl
		}));
	}

});




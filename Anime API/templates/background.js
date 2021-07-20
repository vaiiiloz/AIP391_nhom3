// JavaScript source code

var menuItem = {
	"id":"Anime1",
	"title":"Anime",
	"contexts":["image"]
};

let downloadsArray= [];
let imagePath = [];
let initialState = {
  'savedImages': downloadsArray,
  'imgPath': imagePath
};

chrome.runtime.onInstalled.addListener(function() {
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    chrome.declarativeContent.onPageChanged.addRules([{
      conditions: [
        new chrome.declarativeContent.PageStateMatcher({
          pageUrl: { hostContains: '.google'},
          css: ['img']
        })
      ],
      actions: [ new chrome.declarativeContent.ShowPageAction() ]
    }]);
  });
  chrome.contextMenus.create(menuItem);
  chrome.storage.sync.set(initialState);
  console.log("initialState set");
});

chrome.runtime.onMessage.addListener(
    function(message, callback) {
      console.log("message coming");
      console.log(message);
      let srcArray = message.savedImages;
      var counter = 1;
      var filepaths = ["input.jpg"];
      for (let src of srcArray) {
        chrome.downloads.download({url:src, filename:"input.jpg"});
        console.log(src);
        counter++;
      };

      chrome.storage.local.get("imgPath", function(result){
        result.imgPath = filepaths;
        chrome.storage.local.set(result);
      });
   });



chrome.contextMenus.onClicked.addListener(function(clickData){
	if (clickData.menuItemId == "Anime1"){
	    var src = clickData.srcUrl;
	    chrome.downloads.download({url:src, filename:"input.jpg"});
        console.log(src);
		

        chrome.storage.sync.get("imgPath", function(result){
            var obj = {};
            obj["imgPath"] = src;
            chrome.storage.sync.set(obj, function(){});
          });

        

	}

});




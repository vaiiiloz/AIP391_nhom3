// JavaScript source code
// Console API to clear console before logging new data


const dropArea = document.querySelector(".drag-area");
let dragText = document.getElementById("header");
let button = document.getElementById("browse");
let input = document.getElementById("result");

let file;
function main_init(){
    button.onclick = ()=>{
	
		input.click();
	};


	input.addEventListener("change", function(){
		file = this.files[0];
		showfile();

	});

	dropArea.addEventListener("dragover", (event)=>{
		event.preventDefault();
		dropArea.classList.add("active");
		dragText.textContent = "Release to Upload file";
	});

	dropArea.addEventListener("dragleave", ()=>{
		dropArea.classList.remove("active");
		dragText.textContent = "Drag & Drop to Upload File";
	});

	dropArea.addEventListener("drop", (event)=>{
		event.preventDefault();
	
		file = event.dataTransfer.files[0];
		input.files = event.dataTransfer.files;
		showfile();

	});
};

function ImageExist(url) 
{
   var img = new Image();
   img.src = url;
   return img.height != 0;
}

function downloadfile(){
	fr = new FileReader();
	fr.readAsDataURL(file);
	
}

function showfile(){
	let fileType = file.type;
	
	let validExtensions = ["image/jpeg","image/png","image/jpg"];

	if (validExtensions.includes(fileType)){
		let fileReader = new FileReader();
		
		fileReader.onload = ()=>{
			let fileURL = fileReader.result;
			
			let imgTag = `<img src = "${fileURL}" alt="">`;
			dropArea.innerHTML = imgTag;

			
		}
		fileReader.readAsDataURL(file);

		var blob = new Blob([file],{type:fileType});
		var objectURL = window.URL.createObjectURL(blob);
		var link = document.createElement('a');
		link.href = objectURL;
		link.download = 'input.jpg';
		document.body.appendChild(link);
		link.click();
		link.remove();

		chrome.tabs.executeScript({code : path_add});
	}else{
		alert("This is not an image file");
		dropArea.classList.remove("active");

	}
};

var path_add = 
`
chrome.storage.sync.get('imgPath',function(result){
			paths = [];
			paths.push("Downloads\input.jpg");
			result.imgPath = paths;
			chrome.storage.sync.set(result);
		});

`;

let data = [];

function post_image(url){
	let imgTag = `<img src = "${url}" alt="">`;
	dropArea.innerHTML = imgTag;
};

window.onload = function(){
	
	main_init();
	chrome.storage.sync.get('imgPath', function(result) {
			
			data = result.imgPath;
			

			if (data.length>0){
				post_image(data);
			}
			
		});
	
	
	let upload_button = document.getElementById('upload_button');
	upload_button.onclick = function(){
		chrome.storage.sync.get('imgPath', function(result) {
			
			//data = result.imgPath;
			
		});

		(function(){
			fetch('http://127.0.0.1:5000/upload',{
				method: 'POST',
				header:{
					'Content-Type':'application/json',
				},
				body: JSON.stringify(data),
			})
			.then(respond => 
				respond.json()
				
			)
			.then(data =>{
				console.log('Success',data);
				


				console.log('Hey');
				change_upload(data);
				//window.location.href='upload.html';
			})
			.catch((error) => {
	  			console.error('Error:', error);
			});
		})();
		//
	};
};

function change_upload(upload_data){
    var info = upload_data.info;
	var image_path = upload_data.filename;
	var replacement = {"%image_path%":image_path,"%info%":info};
	var page = upload_html.replace(/%\w+%/g, function(all){
		return replacement[all] || all;
	})
	document.body.parentElement.innerHTML = page;
	var return_button = document.getElementById("return");
	return_button.onclick= ()=>{
	
		document.body.parentElement.innerHTML = main_html;
		input.value = "";
		//main_init();
	};
};




var upload_html =
`
<html>
	<head>
		<meta charset="utf-8"/>
		<meta name = "viewport" content = "width=device-width, initial-scale = 1.0">
		<title>Upload</title>
		<link rel="stylesheet" type = "text/css" href="style.css">
		
	</head>
	<body>
        <p class="text-left"> successfully uploaded.</p>

        <div class = "area">
            <div class = "result-section">
                <div class = "image-section">
                    <div class="image-contain">
                        <img id="image_upload" src="%image_path%" class="upload-image-thumb">
                    </div>
                </div>
                <div class = "info-section">
                    <p id ='info'>%info%</p>
                </div>
            </div>
            <div class ="upload-form">
                
               <p> Upload another?</p>
               <button id = "return">Return</button>
                
            </div>
        </div>

    <script src = "script.js"></script>
    </body>
</html>
`;

var main_html = 
`
<html>
<head>
    <meta charset="utf-8" />
    <meta name = "viewport" content = "width=device-width, initial-scale = 1.0">
    <title>Drag and drop</title>
   <link rel="stylesheet" type = "text/css" href="style.css">

</head>
<body>
    <div class = "drag-area">
        <div class = "icon"><i class = "fas fa-cloud-upload-alt"></i></div>
        <header id = "drag-header"> Drag & Drop to Upload File </header>
        <span> OR </span>
        <button id="browse">Browse file</button>
        <input id = "result" type = "file" name = "file" hidden></input>
        
    </div>
    <div class ="upload-form">
        <button id = "upload_button">Processed </button>
    </div>

    <script src = "script.js"></script>

</body>
</html>
`;
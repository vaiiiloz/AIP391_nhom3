// JavaScript source code
const dropArea = document.querySelector(".drag-area");
dragText = dropArea.querySelector("header");
button = dropArea.querySelector("button");
input = document.querySelector(".result");
let file;

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
	}else{
		alert("This is not an image file");
		dropArea.classList.remove("active");

	}
}
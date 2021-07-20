
export function output(data){
	window.location.href='upload.html';
	var path = window.location.pathname;
	var page = path.split("/").pop();
	console.log( page );
	console.log(data);
	var info = data.info;
	var image_path = data.filename;
	let image_section = document.getElementById("image_upload");
	image_section.src = image_path;

	let info_section = document.getElementById('info');
	info_section.innerHTML = info;
	return 0;
}


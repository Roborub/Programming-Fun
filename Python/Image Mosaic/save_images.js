let link = "";
let count = 0;
let data = [];

document.querySelectorAll("img[src*='encrypted']").forEach(function(e){
	data.push(e.src);
});

let file = new Blob(data);
link = document.createElement("a");
link.setAttribute("download", "fileList.txt");
link.setAttribute("href", URL.createObjectURL(file));
link.click();
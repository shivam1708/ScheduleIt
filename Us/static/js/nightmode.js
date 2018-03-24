var root = document.documentElement;
var nightmode = document.getElementById("nightmode");
var nightmodeDiv = document.getElementsByClassName("nightmode")[0];

nightmodeDiv.addEventListener("click", function(e){
	if(e.target.nodeName=="INPUT"){
		if(nightmode.checked){
			Cookies.set('nightmode',true);
			console.log(Cookies.get('nightmode'),e.target.nodeName);
			root.style.setProperty('--color-primary', '#f56a6a');
			root.style.setProperty('--color-white', '#222');
			root.style.setProperty('--color-white-dark', '#555');
			root.style.setProperty('--color-black', '#fff');
		}
		else {
			Cookies.set('nightmode',false);
			console.log(Cookies.get('nightmode'),e.target.nodeName);
			root.style.setProperty('--color-primary', '#f56a6a');
			root.style.setProperty('--color-white', '#fff');
			root.style.setProperty('--color-white-dark', '#ddd');
			root.style.setProperty('--color-black', '#222');
		};
	}
});
function preLoad(){
	console.log(Cookies.get('nightmode'));
	if(Cookies.get('nightmode')==="true"){
		console.log("xxxxxx");
		nightmode.click();
	}
};
// function preLoad(){
// 	if(active){
// 		nightmode.checked=true;
// 		root.style.setProperty('--color-primary', '#f56a6a');
// 		root.style.setProperty('--color-white', '#222');
// 		root.style.setProperty('--color-white-dark', '#555');
// 		root.style.setProperty('--color-black', '#fff');
// 	}
// 	else{
// 		nightmode.checked=false;
// 		root.style.setProperty('--color-primary', '#f56a6a');
// 		root.style.setProperty('--color-white', '#fff');
// 		root.style.setProperty('--color-white-dark', '#ddd');
// 		root.style.setProperty('--color-black', '#222');	}
// }
window.onload = preLoad();

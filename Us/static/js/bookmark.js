var bookmark=Array.from(document.getElementsByClassName("bookmark"));
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// console.log(bookmark);
function preLoad(){
    bookmark.forEach(function(elem,index){
    var link=document.getElementsByClassName("summarycard__heading")[index].textContent;
    console.log(link,Cookies.get(link));
        if(Cookies.get(link)==="true"){
            elem.classList.remove("fa-bookmark-o");
            elem.classList.add("fa-bookmark");
        }
    })
};

bookmark.forEach(function(elem,index){
    var link=document.getElementsByClassName("summarycard__heading")[index].textContent;
    // Cookies.set(link,false);
	elem.addEventListener("click", function(e){
		e.preventDefault();
        console.log(Cookies.get(link));
		if (Cookies.get(link)==="false"){
            console.log("xxxxxxxxxAAxxxxxx");
            Cookies.set(link,true);
			elem.classList.remove("fa-bookmark-o");
			elem.classList.add("fa-bookmark");
            console.log(Cookies.get(link));
            $.ajax({
                url: bookadd_url,    //Your api url
                type: 'POST',   //type is any HTTP method
                data: {
                    add: link,
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },      //Data as js object
                success: function () {
                }
            });
		}
		else {
            console.log("aaaaaaaaaaaaaaaaaa");
            Cookies.set(link,false);
			elem.classList.remove("fa-bookmark");
			elem.classList.add("fa-bookmark-o");
            $.ajax({
                url: bookrem_url,    //Your api url
                type: 'POST',   //type is any HTTP method
                data: {
                    add: link,
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },      //Data as js object
                success: function () {
                }
            });
		}
	});
});

window.onload = preLoad();

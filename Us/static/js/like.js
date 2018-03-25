var like = Array.from(document.getElementsByClassName("like"));
var unlike = Array.from(document.getElementsByClassName("unlike"));

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

like.forEach(function(elem,index){
    var link=document.getElementsByClassName("summarycard__heading")[index].textContent;
    elem.addEventListener("click", function(e){
		e.preventDefault();
            console.log(link,"likey");
            $.ajax({
                url: like_url,    //Your api url
                type: 'POST',   //type is any HTTP method
                data: {
                    add: link,
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },      //Data as js object
                success: function () {
                }
            });
});
});

unlike.forEach(function(elem,index){
    var link=document.getElementsByClassName("summarycard__heading")[index].textContent;
    elem.addEventListener("click", function(e){
		e.preventDefault();
            console.log(link,"unlike");
            $.ajax({
                url: unlike_url,    //Your api url
                type: 'POST',   //type is any HTTP method
                data: {
                    add: link,
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },      //Data as js object
                success: function () {
                }
            });
});
});
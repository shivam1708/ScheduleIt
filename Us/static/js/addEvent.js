var add=Array.from(document.getElementsByClassName("add"));
var remove=Array.from(document.getElementsByClassName("remove"));

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

add.forEach(function(elem,index){
    var link=document.getElementsByClassName("summarycard__heading")[index].textContent;
    elem.addEventListener("click",function(e){
        e.preventDefault();

        $.ajax({
            url: eventadd_url,    //Your api url
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

remove.forEach(function(elem,index){
    var link=document.getElementsByClassName("summarycard__heading")[index].textContent;
    elem.addEventListener("click",function(e){
        e.preventDefault();

        $.ajax({
            url: eventrem_url,    //Your api url
            type: 'POST',   //type is any HTTP method
            data: {
                add: link,
                csrfmiddlewaretoken: getCookie('csrftoken')
            },      //Data as js object
            success: function () {
            }
        });
    }); 
})
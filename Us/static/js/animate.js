// alert("Connected!");
var submit = document.getElementById("submit");
var input = document.getElementById("subscribe__input");
var tags = document.getElementById("subscribe__list");
var close=[].slice.call(document.getElementsByClassName("close"));
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
close.forEach(function(elem,index){

    elem.addEventListener("click", function(){
        var remove = elem.parentNode;
        var result = elem.parentNode.innerHTML;
        var finalres = result.split("").reverse().slice(54).reverse().join("");
        console.log(finalres);
        tags.removeChild(remove);
            $.ajax({
                url: rem_url,    //Your api url
                type: 'POST',   //type is any HTTP method
                data: {
                    sub: finalres,
                    csrfmiddlewaretoken: getCookie('csrftoken')
                },      //Data as js object
                success: function () {
                }
            });
    });
});
// added manually
// submit.addEventListener("click", function(e){
//  e.preventDefault();
//  var node = document.createElement("DIV");
//  var close = document.createElement("SPAN");
//  node.classList.add("data");
//  close.classList.add("close");
//  close.innerHTML = "x";
//  node.innerHTML = input.value;
//  input.value = "";
//  node.appendChild(close);
//  tags.appendChild(node);
//  close.addEventListener("click", function(){
//      var remove = close.parentNode;
//      var result = close.parentNode.innerHTML;
//      var finalres = result.split("").reverse().slice(28).reverse().join("");
//      console.log(finalres);
//      tags.removeChild(remove);
//             // $.ajax({
//             //     url: 'basic_app/sub/delete',    //Your api url
//             //     type: 'POST',   //type is any HTTP method
//             //     data: {
//             //         data: finalres
//             //     },      //Data as js object
//             //     success: function () {
//             //     }
//             // });
//  });
//  console.log(tags);
// });

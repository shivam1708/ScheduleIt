console.log("connected");
// var submit = document.getElementsByClassName("news__submit")[0];
// var form = document.getElementsByClassName("news__query")[0];
// var res = document.getElementsByClassName("news__result")[0];
// var search = document.getElementsByClassName("news__querysearch")[0];
var add = document.getElementsByClassName("add")[0];

// submit.addEventListener("click", function(){
//     form.classList.add("news__query--animate");
//     setTimeout(function(){
//         res.classList.add("news__result--render");
//     },300);
// });

// search.addEventListener("focus", function(){
//     form.classList.remove("news__query--animate");
//     res.classList.remove("news__result--render");
//     $('.is-open').toggleClass('is-open');
// });

add.addEventListener("click", function(e){
    if(e.target.nodeName == "A" || e.target.nodeName == "LI") {
        console.log("works");
        $('.add__rss').toggleClass('add__rss--open');
    };
});

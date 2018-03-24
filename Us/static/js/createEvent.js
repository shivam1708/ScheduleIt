$(".createEvent__group input").on("focusin",function(){
    $(this).parent().addClass("createEvent__group--active");
})

$(".createEvent__group textarea").on("focusin",function(){
    $(this).parent().addClass("createEvent__group--active");
})

$(".createEvent__group input").on("focusout",function(){
    $(this).parent().removeClass("createEvent__group--active");
})

$(".createEvent__group textarea").on("focusout",function(){
    $(this).parent().removeClass("createEvent__group--active");
})

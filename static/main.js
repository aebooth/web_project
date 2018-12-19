$(document).ready(function(){
    $("#nocake").hide();
    
    $("#cake").click(function(e){
        $(this).slideUp();
        $("#nocake").slideDown();
    })
    
    $("#nocake").click(function(e){
        $(this).slideUp();
        $("#cake").slideDown();
    })
});
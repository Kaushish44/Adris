$(document).ready(function(){
$("#txtSearch").keyup( function(){
	
        var value = $('#txtSearch').val();
        $.ajax({
        	url: "autocomplete",
         	data: { 'q': value },
            dataType: 'json',
            success: function (data) {
                res = data.results;
                $("#txtSearch").autocomplete({
                source: res,
                minLength: 1,
                }); 
            }
        });     
    });
});
var total = 0;
var q;
var description = '';
var ids = {};
var ip = {};

function minus(price,desc){
	description = '';
	if (!ids[desc]){
		alert('Item not in the order');
		return;
	}
	ids[desc] -= 1;
	//remove item from order
	if (ids[desc] == 0){
		delete ids[desc];
	}
	document.getElementById("orders").innerHTML = 'Orders'; // when no item present in order
	//print all the ordered items.
	for(var d in ids) {
	    q = ids[d]
	    description += d + ' ' + q + ', '
	    document.getElementById("orders").innerHTML = description;
	}
	total -= price;
	document.getElementById("total").innerHTML = total;
}

function plus(price,desc){
	description = '';
	total += price;
	if(desc in ids) {
	    // exist
		var c = ids[desc];
		c += 1;
		ids[desc]=c;
	}
	else {
	    // does not exist
		ids[desc]=1;
		ip[desc]=price;//storing item prices
	}
	//print all the ordered items.
	for(var d in ids) {
	    q = ids[d];
	    description += d + ' ' + q + ', ';
	    document.getElementById("orders").innerHTML = description;
	}
	//print total amount
	document.getElementById("total").innerHTML = total;
	
}

function reset_bill(){
	total = 0;
	description = '';
	ids = {};
	ip = {};
	document.getElementById("orders").innerHTML = 'Orders:';
	document.getElementById("total").innerHTML = 'Total:';
}

function generate_bill(){
	var displayOrder = '';
	var itemPrice = 0;
	//need to add taxes to total amount
	document.getElementById("orderBill").innerHTML = "The total Bill of Order is: " + total;
	for(var d in ids) {
		itemPrice = ip[d];
	    q = ids[d];
	    displayOrder += d +  ' x ' + q + ' = ' + itemPrice*q + "<br />";
	}
	document.getElementById("details").innerHTML = displayOrder;//need to display taxes
}

function submit_bill(){
	if (total==0){
		alert("The Bill Amount is 0");
		return 0;
	}
	if (confirm("Submit the Bill?") == true) {
        $.ajax({
        	url:"submitBill",
        	dataType: "json",
        	data:{'billAmount':total, 'ids':JSON.stringify(ids)},
        	success: function(data){
        		$("#myModal .close").click();
        	}
        });
        reset_bill();
    } 
}
frappe.provide('erpnext');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	$('.navbar-home').html('<img class="erpnext-icon" src="'+
			frappe.urllib.get_base_url()+'/assets/seef/images/seef_logo.jpg"/>');
});
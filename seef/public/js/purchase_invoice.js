frappe.ui.form.on('Purchase Invoice', {
	refresh: function(frm) {
        if (frm.doc.docstatus === 0) {
            
            
			frm.add_custom_button(__('Material Request'),
				function() {
					console.log("gggggggg");
				}, __("Get items from"));
		} 
    }
});
	 
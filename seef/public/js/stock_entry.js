
frappe.ui.form.on('Stock Entry', {
	purpose: function(frm) {
        frm.toggle_enable("to_warehouse", 1);
    }
});
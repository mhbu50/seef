
frappe.ui.form.on("Journal Entry Account", {
	debit_in_account_currency:function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        if(row.debit != 0 && row.credit > 0){
            frappe.model.set_value(row.doctype, row.name, "credit", 0);
            frappe.model.set_value(row.doctype, row.name, "credit_in_account_currency", 0);
        }      
    },
    credit_in_account_currency:function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        if(row.credit != 0 && row.debit > 0){
            frappe.model.set_value(row.doctype, row.name, "debit", 0);
            frappe.model.set_value(row.doctype, row.name, "debit_in_account_currency", 0);
        }        
    },
    accounts_add: function(doc, cdt, cdn) {
		var row = frappe.get_doc(cdt, cdn);
				row.credit_in_account_currency = 0
				row.credit = 0;
				row.debit_in_account_currency = 0;
				row.debit = 0;
	}
});

frappe.ui.form.on('Sales Invoice', {
    before_submit: function (frm) {
        console.log("on_submit")
      //set cosnter for items
      frm.doc.items.forEach(function (d) {
        frappe.model.set_value(d.doctype, d.name, "cost_center", frm.doc.cost_center);
      });
      //set cost center for tax
      frm.doc.taxes.forEach(function (d) {
        frappe.model.set_value(d.doctype, d.name, "cost_center", frm.doc.cost_center);
      });
    }  
  });
  
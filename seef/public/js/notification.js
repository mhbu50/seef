$(document).on('app_ready', function() {
  if (!frappe.boot.consoleerp || frappe.get_route()[0] != "")
    return;

  if (frappe.boot.consoleerp.expiring_documents && frappe.boot.consoleerp.expiring_documents.length > 0) {
    // var rows = frappe.boot.consoleerp.expiring_documents.reduce(function(str, obj) {
    //   return str +
    //     "<tr>" +
    //     "<td>" + obj + "</td>" +
    //     "<td>" + obj.type + "</td>" +
    //     "<td>" + obj.expiry_date + "</td>" +
    //     "<td>" +
    //     "<a data-parent='" + obj.parent + "' data-parenttype='" + obj.parenttype + "'>" +
    //     obj.parenttype +
    //     "-" +
    //     obj.parent +
    //     "</a>" +
    //     "</td>" +
    //     "</tr>";
    // }, "");
    // var $wrapper = frappe.msgprint("<h3>Expiring Documents</h3>" +
    //   "<br>The following documents will expire soon." +
    //   "<table class='table table-striped table-hover'>" +
    //   "<thead>" +
    //   "<tr>" +
    //   "<th>" + __("Doc No") + "</th>" +
    //   "<th>" + __("Type") + "</th>" +
    //   "<th>" + __("Expiry Date") + "</th>" +
    //   "<th>" + __("Parent") + "</th>" +
    //   "</tr>" +
    //   "</thead>" +
    //   "<tbody>" +
    //   rows +
    //   "</tbody>" +
    //   "</table>" +
    //   "<hr>", "Console ERP Notifications").$wrapper;
    // $wrapper.find("a").on("click", function() {
    //   frappe.set_route("Form", $(this).data("parenttype"), $(this).data("parent"));
    // })

    // show only once
    //frappe.boot.consoleerp.expiring_documents = null;
    if (in_list(frappe.user_roles,'Accounts User', 'Accounts Manager')) {
      var dialog = new frappe.ui.Dialog({
        title: __("Set Company"),
        fields: [
          {
            "fieldtype": "Link",
            "label": __("Company"),
            "fieldname": "company",
            "options": "Company",
            "reqd": 1
          }
        ],primary_action: function() {
          var data = dialog.get_values();
  						dialog.hide();
              console.log("gggggg");
  						return frappe.call({
  							method: "frappe.client.set_value",
  							args: {
  								doctype: "User Permission",
  								name: {'user':frappe.session.user,'allow':'Company'},
                  fieldname: 'for_value',
                  value: data.company
  							},
  							callback: function() { }
  						});
  					},
  					primary_action_label: __('Save')
      });
      dialog.show();
    }
  }
});
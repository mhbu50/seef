frappe.provide("accurate.ui");

accurate.ui.set_company = function() {
    const {
        message: { batch_no_details, uom_details, exchange_rates } = {},
      }  = await frappe.call({ method: 'seef.seef_app.tools.get_avalabil_company' });
    if (message) {
        console.log("me",message);
        
    }
    var dialog = new frappe.ui.Dialog({
        title: __("Set Company"),
        fields: [{
            "fieldtype": "Select",
            "label": __("Company"),
            "fieldname": "company",
            "options": message,
            "reqd": 1
        }],
        primary_action: function() {
            var data = dialog.get_values();
            dialog.hide();
            frappe.db.get_value("User Permission", { 'user': frappe.session.user, 'allow': 'Company' }, 'name', function(r) {
                frappe.db.set_value("User Permission", r.name, "for_value", data.company, function(r) {
                    console.log('befor reload page');
                    //set expires cookie
                    var date = new Date();
                    date.setTime(date.getTime() + (1 * 24 * 60 * 60 * 1000));
                    var expires = "; expires=" + date.toUTCString();
                    document.cookie = "company" + "=" + (data.company || "") + expires + "; path=/";
                    window.location.reload();
                });
            })
        },
        primary_action_label: __('Save')
    });
    dialog.show();
}

$(document).on('app_ready', function() {

    setTimeout(function() {
        frappe.app.logout = (function(_super) {
            return function() {
                document.cookie = 'company=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
                return _super.apply(this, arguments);
            };
        })(frappe.app.logout);
    }, 3000);
    $('<li><a href="#" onclick="accurate.ui.set_company();return false;"> ' + __("Set Company") + '</a></li>').insertAfter($('.navbar-set-desktop-icons').next());

    if (in_list(frappe.user_roles, 'Accounts User', 'Accounts Manager') &&
        !in_list(frappe.user_roles, 'System Manager') &&
        frappe.get_cookie("company") == undefined) {
        accurate.ui.set_company();
    }

});
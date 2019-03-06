class TreeView extends frappe.views.TreeView {
    new_node() {
        super.new_node();
        var tree_account_name = cur_tree.get_selected_node().label;
        setTimeout(function() {
                frappe.call({
                    method: "seef.seef_app.tools.get_new_account_number",
                    args: {
                        account_name: tree_account_name,
                        is_group: cur_dialog.get_value("is_group")
                    },
                    callback: function(r, rt) {
                        cur_dialog.set_value("account_number", r.message)
                    }
                });
                cur_dialog.fields_dict.is_group.$wrapper.on("change", function(v) {
                    console.log("cur_tree.get_selected_node().label", tree_account_name)
                    frappe.call({
                        method: "seef.seef_app.tools.get_new_account_number",
                        args: {
                            account_name: tree_account_name,
                            is_group: cur_dialog.get_value("is_group")
                        },
                        callback: function(r, rt) {
                            cur_dialog.set_value("account_number", r.message)
                        }
                    });
                })
            },
            1000);
    }
}

frappe.views.TreeView = TreeView;
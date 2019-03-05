
from __future__ import unicode_literals
import frappe
import json
from frappe import _
from erpnext import get_default_company
from frappe.model.document import Document
from frappe.utils import flt, today, getdate, add_years
from frappe.model.document import Document
from frappe.desk.notifications import get_filters_for

@frappe.whitelist()
def get_material_request(source_name, target_doc=None, ignore_permissions=False):
	def postprocess(source, target):
		pass

	def set_missing_values(source, target):
		target.run_method("calculate_taxes_and_totals")

		# set company address
		target.update(get_company_address(target.company))
		# if target.company_address:
		# 	target.update(get_fetch_values("Sales Invoice", 'company_address', target.company_address))

	def update_item(source, target, source_parent):
		target.amount = flt(source.amount) - flt(source.billed_amt)
		target.base_amount = target.amount * flt(source_parent.conversion_rate)
		target.qty = target.amount / flt(source.rate) if (source.rate and source.billed_amt) else source.qty

		item = frappe.db.get_value("Item", target.item_code, ["item_group", "selling_cost_center"], as_dict=1)
		target.cost_center = frappe.db.get_value("Project", source_parent.project, "cost_center") \
			or item.selling_cost_center \
			or frappe.db.get_value("Item Group", item.item_group, "default_cost_center")

	doclist = get_mapped_doc("Sales Order", source_name, {
		"Sales Order": {
			"doctype": "Sales Invoice",
			"field_map": {
				"party_account_currency": "party_account_currency"
			},
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Material Request Item": {
			"doctype": "Purchase Invoice Item",
			"field_map": {
				"name": "so_detail",
				"parent": "sales_order",
			}
		}
	}, target_doc, postprocess, ignore_permissions=ignore_permissions)

	return doclist

def boot_session(bootinfo):
	bootinfo["consoleerp"] = {
		"expiring_documents": [1,2,3,4,5,6]
	}

	# startup messages

	# keep existing messages
	if "messages" in bootinfo and not isinstance(bootinfo["messages"], list):
		bootinfo["messages"] = [bootinfo["messages"]]
	bootinfo["messages"] = bootinfo.get("messages", [])
	companies = [d['name'] for d in frappe.get_list("Company")]
	# bootinfo["messages"].append(companies)

	return bootinfo

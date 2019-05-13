
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


@frappe.whitelist()
def get_new_account_number(account_name, is_group=1):
	#child_seed=0
	leaf_seed = 0
	parent_account = frappe.db.get_value(
		"Account", account_name, "parent_account")
	last_acct_num = frappe.get_all('Account', fields=['account_number'], filters={
	                               'parent_account': account_name, 'is_group': int(is_group)}, order_by='account_number desc', limit=1)
	if (last_acct_num):
		last_acct_num = last_acct_num[0]['account_number']

	account_number = frappe.db.get_value(
		"Account", account_name, "account_number")
	leaf_node_count = frappe.db.count(
		'Account', filters={'parent_account': parent_account, 'is_group': 0})
	#child
	if (is_group == '1'):
		if (last_acct_num != None and last_acct_num != '' and last_acct_num != []):
			child_seed = (int(last_acct_num) % 10)+1

		else:
			child_seed = 1
		new_account_number = str(account_number)+str(child_seed)
		return new_account_number

	#leaf
	if (is_group == '0'):
		if (last_acct_num != None and last_acct_num != '' and last_acct_num != []):
			if (leaf_node_count > 9):
				str_num = str(last_acct_num)
				if (str_num.endswith('0', len(str_num)-2, len(str_num)-1)):
					leaf_seed = (int(last_acct_num) % 10)+1
					new_account_number = str(account_number)+str("{0:0>2}".format(leaf_seed))
				else:
					leaf_seed = (int(last_acct_num) % 100)+1
					new_account_number = str(account_number)+str(leaf_seed)
			else:
				leaf_seed = (int(last_acct_num) % 10)+1
				new_account_number = str(account_number)+str("{0:0>2}".format(leaf_seed))
		else:
			leaf_seed = 1
			new_account_number = str(account_number)+str("{0:0>2}".format(leaf_seed))
		frappe.errprint(new_account_number)
		return new_account_number


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

@frappe.whitelist()
def get_avalabil_company():
	select_company = []
	all_company = frappe.get_all("Company", fields=["name"])
	all_company = [d['name'] for d in all_company]
	permission_company = frappe.get_all(
            "User Permission", fields=["for_value"], filters={"allow": "Company"})
	permission_company = [d['for_value'] for d in permission_company]
	select_company = intersection(all_company, permission_company)
	return select_company
	# return [d['name'] for d in all_company]

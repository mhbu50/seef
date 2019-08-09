# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '0.0.5'

from six import iteritems
import erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts
from frappe.core.doctype.file.file import File
from frappe.utils import get_site_path


def create_charts(company, chart_template=None, existing_company=None, custom_chart=None):
	chart = custom_chart or get_chart(chart_template, existing_company)
	if chart:
		accounts = []

		def _import_accounts(children, parent, root_type, root_account=False):
			for account_name, child in iteritems(children):
				if root_account:
					root_type = child.get("root_type")

				if account_name not in ["account_number", "account_type",
					"root_type", "is_group", "tax_rate"]:

					account_number = cstr(child.get("account_number")).strip()
					account_name, account_name_in_db = add_suffix_if_duplicate(account_name,
						account_number, accounts)

					is_group = identify_is_group(child)
					report_type = "Balance Sheet" if root_type in ["Asset", "Liability", "Equity"] \
						else "Profit and Loss"

					account = frappe.get_doc({
						"doctype": "Account",
						"account_name": account_name,
						"company": company,
						"parent_account": parent,
						"is_group": is_group,
						"root_type": root_type,
						"report_type": report_type,
						"account_number": account_number,
						"account_type": child.get("account_type"),
						"account_currency": child.get('account_currency') or frappe.db.get_value('Company',  company,  "default_currency"),
						"tax_rate": child.get("tax_rate")
					})

					if root_account or frappe.local.flags.allow_unverified_charts:
						account.flags.ignore_mandatory = True

					account.flags.ignore_permissions = True

					account.insert()

					accounts.append(account_name_in_db)

					_import_accounts(child, account.name, root_type)

		# Rebuild NestedSet HSM tree for Account Doctype
		# after all accounts are already inserted.
		frappe.local.flags.ignore_on_update = True
		_import_accounts(chart, None, None, root_account=True)
		rebuild_tree("Account", "parent_account")
		frappe.local.flags.ignore_on_update = False

def identify_is_group(child):
	if child.get("is_group"):
		is_group = child.get("is_group")
	elif len(set(child.keys()) - set(["account_type", "root_type", "is_group", "tax_rate", "account_number"])):
		is_group = 1
	else:
		is_group = 0

	return is_group
	
@frappe.whitelist()
def build_tree_from_json(chart_template, chart_data=None):
	''' get chart template from its folder and parse the json to be rendered as tree '''
	chart = chart_data or get_chart(chart_template)

	# if no template selected, return as it is
	if not chart:
		return

	accounts = []
	def _import_accounts(children, parent):
		''' recursively called to form a parent-child based list of dict from chart template '''
		for account_name, child in iteritems(children):
			account = {}
			if account_name in ["account_number", "account_type",\
				"root_type", "is_group", "tax_rate"]: continue

			account['parent_account'] = parent
			account['expandable'] = True if identify_is_group(child) else False
			account['value'] = (child.get('account_number') + ' - ' + account_name) \
				if child.get('account_number') else account_name
			accounts.append(account)
			_import_accounts(child, account['value'])

	_import_accounts(chart, None)
	return accounts

def get_files_path(*path, **kwargs):
	return get_site_path("private" if kwargs.get("is_private") else "public", "files", *path)

def get_full_path(self):
    """Returns file path from given file name"""

    file_path = self.file_url or self.file_name

    if "/" not in file_path:
        file_path = "/files/" + file_path

    if file_path.startswith("/private/files/"):
        file_path = get_files_path(*file_path.split("/private/files/", 1)[1].split("/"), is_private=1)

    elif file_path.startswith("/files/"):
        file_path = get_files_path(*file_path.split("/files/", 1)[1].split("/"))

    elif file_path.startswith("http"):
        pass

    elif not self.file_url:
        frappe.throw(_("There is some problem with the file url: {0}").format(file_path))

    return file_path

erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.create_charts = create_charts
erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.build_tree_from_json = build_tree_from_json
File.get_full_path = get_full_path